from fastapi import APIRouter

from api.v1.routers import (
	autenticacao,
	dres,
	projetos_sociais,
	projetos_sociais_escolares,
	ues,
    usuarios,
	formularios,
    campos,
	categorias,
	publicos_alvos,
    dashboard,
)


api_router = APIRouter()
api_router.include_router(autenticacao.router, prefix="/autenticacao", tags=["Autenticacao"])
api_router.include_router(categorias.router, prefix='/categorias', tags=['Categorias'])
api_router.include_router(campos.router, prefix='/campos', tags=['Campos'])
api_router.include_router(dashboard.router, prefix='/dashboard', tags=['Dashboard'])
api_router.include_router(dres.router, prefix='/dres', tags=['Dres'])
api_router.include_router(formularios.router, prefix='/formularios', tags=['Formularios'])
api_router.include_router(projetos_sociais.router, prefix='/projetos-sociais', tags=['Projetos Sociais'])
api_router.include_router(projetos_sociais_escolares.router, prefix='/projetos-sociais-escolares', tags=['Projetos Sociais Escolares'])
api_router.include_router(publicos_alvos.router, prefix='/publicos-alvos', tags=['Publicos Alvos'])
api_router.include_router(ues.router, prefix='/ues', tags=['Ues'])
api_router.include_router(usuarios.router, prefix='/usuarios', tags=['Usuarios'])