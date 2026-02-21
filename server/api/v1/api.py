from fastapi import APIRouter

from api.v1.routers import (
	autenticacao,
	dres,
	projetos_sociais,
	projetos_sociais_escolares,
	ues,
    usuarios,
	situacoes,
	publicos_alvos,
)


api_router = APIRouter()
api_router.include_router(autenticacao.router, prefix="/autenticacao", tags=["Autenticacao"])
api_router.include_router(dres.router, prefix='/dres', tags=['Dres'])
api_router.include_router(ues.router, prefix='/ues', tags=['Ues'])
api_router.include_router(projetos_sociais.router, prefix='/projetos-sociais', tags=['Projetos Sociais'])
api_router.include_router(projetos_sociais_escolares.router, prefix='/projetos-sociais-escolares', tags=['Projetos Sociais Escolares'])
api_router.include_router(usuarios.router, prefix='/usuarios', tags=['Usuarios'])
api_router.include_router(situacoes.router, prefix='/situacoes', tags=['Situacoes'])
api_router.include_router(publicos_alvos.router, prefix='/publicos-alvos', tags=['Publicos Alvos'])