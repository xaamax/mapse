from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import ProjetoSocial
from repositories import ProjetoSocialRepository
from schemas import (
    ProjetoSocialListPaginated,
    ProjetoSocialPartial,
    ProjetoSocialPublic,
    ProjetoSocialSchema,
)
from services import ProjetoSocialService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> ProjetoSocialService:
    return ProjetoSocialService(ProjetoSocialRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ProjetoSocialPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_projeto_social(
    payload: ProjetoSocialSchema,
    service: ProjetoSocialService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=ProjetoSocialListPaginated,
)
async def list_projetos_sociais(
    page_number: int = 1,
    page_size: int = 10,
    service: ProjetoSocialService = Depends(get_service),
):
    return await service.list(page_number=page_number, page_size=page_size)


@router.get(
    "/{id}",
    response_model=ProjetoSocialSchema,
    responses={404: {"model": ErrorResponse}},
)
async def get_projeto_social(
    id: int,
    service: ProjetoSocialService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=ProjetoSocialSchema,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_projeto_social(
    id: int,
    payload: ProjetoSocialSchema,
    service: ProjetoSocialService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=ProjetoSocialPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_projeto_social(
    id: int,
    payload: ProjetoSocialPartial,
    service: ProjetoSocialService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_projeto_social(
    id: int,
    service: ProjetoSocialService = Depends(get_service),
):
    await service.delete(id)
