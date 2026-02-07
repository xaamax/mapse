from fastapi import APIRouter

from api.v1.routers import dres, ues

api_router = APIRouter()
api_router.include_router(dres.router, prefix='/dres', tags=['Dres'])
api_router.include_router(ues.router, prefix='/ues', tags=['Ues'])