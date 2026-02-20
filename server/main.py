from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from core.exception_handlers import generic_exception_handler
from core.configs import settings

from api.v1.api import api_router


app = FastAPI(
    title='MAPSE API',
    description='API de Sistema de Mapeamento de Projetos Sociais nas Escolas',
    version='0.1.0',
)

app.include_router(api_router, prefix=settings.API_V1_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, generic_exception_handler)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})
    openapi_schema["components"]["securitySchemes"]["Bearer"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }

    # Remove any other security schemes (e.g. OAuth2) so only Bearer appears
    sec_schemes = openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})
    for key in list(sec_schemes.keys()):
        if key != "Bearer":
            del sec_schemes[key]

    for path, methods in openapi_schema.get("paths", {}).items():
        for method_name, method in methods.items():
            if path.startswith(settings.API_V1_URL + "/autenticacao"):
                continue
            method.setdefault("security", [])
            if {"Bearer": []} not in method["security"]:
                method["security"].append({"Bearer": []})

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

