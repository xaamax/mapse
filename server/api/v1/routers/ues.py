from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import Ue
from repositories import UeRepository
from schemas import (
    UeCompact,
    UeListPaginated,
    UePartial,
    UePublic,
    UeSchema,
)
from services import UeService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> UeService:
    return UeService(UeRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UePublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_ue(
    payload: UeSchema,
    service: UeService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=UeListPaginated,
)
async def list_ues(
    page_number: int = 1,
    page_size: int = 10,
    service: UeService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(Ue),
        page_number=page_number,
        page_size=page_size,
    )


@router.get(
    "/por-dre/{codigo_dre}",
    response_model=list[UeCompact],
)
async def get_ues_por_dre(
    codigo_dre: str,
    service: UeService = Depends(get_service),
):
    return await service.get_by_codigo_dre(codigo_dre)


@router.get(
    "/{id}",
    response_model=UePublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_ue(
    id: int,
    service: UeService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=UePublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_ue(
    id: int,
    payload: UeSchema,
    service: UeService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=UePublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_ue(
    id: int,
    payload: UePartial,
    service: UeService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_ue(
    id: int,
    service: UeService = Depends(get_service),
):
    await service.delete(id)
