from fastapi import APIRouter

from api.v1.routers import dres

api_router = APIRouter()
api_router.include_router(dres.router, prefix='/dres', tags=['Dres'])