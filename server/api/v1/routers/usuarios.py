from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from models import Usuario
from repositories import UsuarioRepository
from services import UsuarioService
from schemas import UsuarioSchema, UsuarioPartial, UsuarioPublic, UsuarioListPaginated

from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> UsuarioService:
    return UsuarioService(UsuarioRepository(session))


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UsuarioPublic)
async def create_usuario(
    payload: UsuarioSchema,
    service: UsuarioService = Depends(get_service),
):
    return await service.create(payload)



@router.get(
    "",
    response_model=UsuarioListPaginated,
)
async def list_usuarios(
    page_number: int = 1,
    page_size: int = 10,
    service: UsuarioService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(Usuario),
        page_number=page_number,
        page_size=page_size,
    )


@router.get(
    "/{id}",
    response_model=UsuarioPublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_usuario(
    id: int,
    service: UsuarioService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=UsuarioPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_usuario(
    id: int,
    payload: UsuarioSchema,
    service: UsuarioService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=UsuarioPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_usuario(
    id: int,
    payload: UsuarioPartial,
    service: UsuarioService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_usuario(
    id: int,
    service: UsuarioService = Depends(get_service),
):
    await service.delete(id)
