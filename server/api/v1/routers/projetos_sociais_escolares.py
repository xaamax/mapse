from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from models import ProjetoSocialEscolar
from repositories import ProjetoSocialEscolarRepository
from schemas import (
    ProjetoSocialEscolarListPaginated,
    ProjetoSocialEscolarPartial,
    ProjetoSocialEscolarPublic,
    ProjetoSocialEscolarSchema,
)
from services import ProjetoSocialEscolarService

router = APIRouter()


def get_service(
    session: AsyncSession = Depends(get_session),
) -> ProjetoSocialEscolarService:
    return ProjetoSocialEscolarService(ProjetoSocialEscolarRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ProjetoSocialEscolarPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_projeto_social_escolar(
    payload: ProjetoSocialEscolarSchema,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=ProjetoSocialEscolarListPaginated,
)
async def list_projetos_sociais_escolares(
    page_number: int = 1,
    page_size: int = 10,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await paginate_response(
        session=service.repository.session,
        query=select(ProjetoSocialEscolar),
        page_number=page_number,
        page_size=page_size,
    )


@router.get(
    "/{id}",
    response_model=ProjetoSocialEscolarPublic,
    responses={404: {"model": ErrorResponse}},
)
async def get_projeto_social_escolar(
    id: int,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await service.get(id)


@router.put(
    "/{id}",
    response_model=ProjetoSocialEscolarPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_projeto_social_escolar(
    id: int,
    payload: ProjetoSocialEscolarSchema,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=ProjetoSocialEscolarPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_projeto_social_escolar(
    id: int,
    payload: ProjetoSocialEscolarPartial,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_projeto_social_escolar(
    id: int,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    await service.delete(id)
