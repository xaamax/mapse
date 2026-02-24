from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.schemas import ErrorResponse

from repositories import CampoRepository
from models import (
    CampoSchema,
    CampoListPaginated,
    CampoPartial,
    CampoPublic,
    TipoCampoEnum,
)
from services import CampoService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> CampoService:
    return CampoService(CampoRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=CampoPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_campo(
    payload: CampoSchema,
    service: CampoService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=CampoListPaginated,
)
async def list_campos(
    page_number: int = 1,
    page_size: int = 10,
    service: CampoService = Depends(get_service),
):
    return await service.list(page_number=page_number, page_size=page_size)

@router.get(
    "/tipos",
)
async def tipos_campos():
    return [{"label": t.label, "value": t.value} for t in TipoCampoEnum]


@router.get(
    "/{id}",
    response_model=CampoSchema,
    responses={404: {"model": ErrorResponse}},
)
async def get_campo(
    id: int,
    service: CampoService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=CampoSchema,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_campo(
    id: int,
    payload: CampoSchema,
    service: CampoService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=CampoPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_campo(
    id: int,
    payload: CampoPartial,
    service: CampoService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_campo(
    id: int,
    service: CampoService = Depends(get_service),
):
    await service.delete(id)
