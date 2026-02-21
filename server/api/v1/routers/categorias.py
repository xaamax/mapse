from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import Categoria
from repositories import CategoriaRepository
from schemas import (
    CategoriaCompact,
    CategoriaListPaginated,
    CategoriaPartial,
    CategoriaPublic,
    CategoriaSchema,
)
from services import CategoriaService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> CategoriaService:
    return CategoriaService(CategoriaRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_categoria(
    payload: CategoriaSchema,
    service: CategoriaService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=CategoriaListPaginated,
)
async def list_categorias(
    page_number: int = 1,
    page_size: int = 10,
    service: CategoriaService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(Categoria),
        page_number=page_number,
        page_size=page_size,
    )


@router.get(
    "/opcoes",
    response_model=list[CategoriaCompact],
    responses={404: {"model": ErrorResponse}},
)
async def get_categorias(
    service: CategoriaService = Depends(get_service),
):
    return await service.listar_categorias()


@router.get(
    "/{id}",
    response_model=CategoriaPublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_categoria(
    id: int,
    service: CategoriaService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=CategoriaPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_categoria(
    id: int,
    payload: CategoriaSchema,
    service: CategoriaService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=CategoriaPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_categoria(
    id: int,
    payload: CategoriaPartial,
    service: CategoriaService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_categoria(
    id: int,
    service: CategoriaService = Depends(get_service),
):
    await service.delete(id)
