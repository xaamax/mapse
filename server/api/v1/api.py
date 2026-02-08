from fastapi import APIRouter

from api.v1.routers import dres, ues, projetos_sociais, projetos_sociais_escolares

api_router = APIRouter()
api_router.include_router(dres.router, prefix='/dres', tags=['Dres'])
api_router.include_router(ues.router, prefix='/ues', tags=['Ues'])
api_router.include_router(projetos_sociais.router, prefix='/projetos_sociais', tags=['Projetos Sociais'])
api_router.include_router(projetos_sociais_escolares.router, prefix='/projetos_sociais_escolares', tags=['Projetos Sociais Escolares'])