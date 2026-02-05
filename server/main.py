from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

