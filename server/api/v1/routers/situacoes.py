from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import Situacao
from repositories import SituacaoRepository
from schemas import (
    SituacaoCompact,
    SituacaoListPaginated,
    SituacaoPartial,
    SituacaoPublic,
    SituacaoSchema,
)
from services import SituacaoService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> SituacaoService:
    return SituacaoService(SituacaoRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=SituacaoPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_situacao(
    payload: SituacaoSchema,
    service: SituacaoService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=SituacaoListPaginated,
)
async def list_situacoes(
    page_number: int = 1,
    page_size: int = 10,
    service: SituacaoService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(Situacao),
        page_number=page_number,
        page_size=page_size,
    )

@router.get(
    "/opcoes",
    response_model=list[SituacaoCompact],
    responses={404: {"model": ErrorResponse}},
)
async def get_situacoes(
    service: SituacaoService = Depends(get_service),
):
    return await service.listar_situacoes()

@router.get(
    "/{id}",
    response_model=SituacaoPublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_situacao(
    id: int,
    service: SituacaoService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=SituacaoPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_situacao(
    id: int,
    payload: SituacaoSchema,
    service: SituacaoService = Depends(get_service),
):
    return await service.update(id, payload)

@router.patch(
    "/{id}",
    response_model=SituacaoPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_situacao(
    id: int,
    payload: SituacaoPartial,
    service: SituacaoService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_situacao(
    id: int,
    service: SituacaoService = Depends(get_service),
):
    await service.delete(id)
