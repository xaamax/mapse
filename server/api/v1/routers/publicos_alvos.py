from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import PublicoAlvo
from repositories import PublicoAlvoRepository
from schemas import (
    PublicoAlvoCompact,
    PublicoAlvoListPaginated,
    PublicoAlvoPartial,
    PublicoAlvoPublic,
    PublicoAlvoSchema,
)
from services import PublicoAlvoService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> PublicoAlvoService:
    return PublicoAlvoService(PublicoAlvoRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PublicoAlvoPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_publico_alvo(
    payload: PublicoAlvoSchema,
    service: PublicoAlvoService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=PublicoAlvoListPaginated,
)
async def list_publicos_alvos(
    page_number: int = 1,
    page_size: int = 10,
    service: PublicoAlvoService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(PublicoAlvo),
        page_number=page_number,
        page_size=page_size,
    )

@router.get(
    "/opcoes",
    response_model=list[PublicoAlvoCompact],
    responses={404: {"model": ErrorResponse}},
)
async def get_publicos_alvos_opcoes(
    service: PublicoAlvoService = Depends(get_service),
):
    return await service.listar_publicos_alvos()


@router.get(
    "/{id}",
    response_model=PublicoAlvoPublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_publico_alvo(
    id: int,
    service: PublicoAlvoService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=PublicoAlvoPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_publico_alvo(
    id: int,
    payload: PublicoAlvoSchema,
    service: PublicoAlvoService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=PublicoAlvoPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_publico_alvo(
    id: int,
    payload: PublicoAlvoPartial,
    service: PublicoAlvoService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_publico_alvo(
    id: int,
    service: PublicoAlvoService = Depends(get_service),
):
    await service.delete(id)
