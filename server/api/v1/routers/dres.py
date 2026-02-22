from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from core.security import get_current_user

from models import Dre
from repositories import DreRepository
from models import (
    DreCompact,
    DreListPaginated,
    DrePartial,
    DrePublic,
    DreSchema,
)
from services import DreService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> DreService:
    return DreService(DreRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=DrePublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_dre(
    payload: DreSchema,
    service: DreService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=DreListPaginated,
)
async def list_dres(
    page_number: int = 1,
    page_size: int = 10,
    service: DreService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(Dre),
        page_number=page_number,
        page_size=page_size,
    )

@router.get(
    "/codigos-dres",
    response_model=list[DreCompact],
    responses={404: {"model": ErrorResponse}},
)
async def get_codigos_nomes(
    service: DreService = Depends(get_service),
):
    return await service.listar_codigo_dre_nome()

@router.get(
    "/{id}",
    response_model=DrePublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_dre(
    id: int,
    service: DreService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=DrePublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_dre(
    id: int,
    payload: DreSchema,
    service: DreService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=DrePublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_dre(
    id: int,
    payload: DrePartial,
    service: DreService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_dre(
    id: int,
    service: DreService = Depends(get_service),
):
    await service.delete(id)