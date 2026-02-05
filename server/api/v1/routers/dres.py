from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import Dre
from repositories import DreRepository
from schemas import (
    DreListPaginated,
    DrePartial,
    DrePublic,
    DreSchema,
)
from services import DreService

router = APIRouter()


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
    "/{codigo_dre}",
    response_model=DrePublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_dre(
    codigo_dre: int,
    service: DreService = Depends(get_service),
):
    return await service.get(codigo_dre)


@router.put(
    "/{codigo_dre}",
    response_model=DrePublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_dre(
    codigo_dre: int,
    payload: DreSchema,
    service: DreService = Depends(get_service),
):
    return await service.update(codigo_dre, payload)


@router.patch(
    "/{codigo_dre}",
    response_model=DrePublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_dre(
    codigo_dre: int,
    payload: DrePartial,
    service: DreService = Depends(get_service),
):
    return await service.patch(codigo_dre, payload)


@router.delete(
    "/{codigo_dre}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_dre(
    codigo_dre: int,
    service: DreService = Depends(get_service),
):
    await service.delete(codigo_dre)
