from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user


from shared.pagination import paginate_response
from shared.schemas import ErrorResponse

from repositories import ProjetoSocialEscolarRepository
from schemas import (
    ProjetoSocialEscolarSave,
    ProjetoSocialEscolarSchema,
    ProjetoSocialEscolarListPaginated,
)
from services import ProjetoSocialEscolarService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> ProjetoSocialEscolarService:
    return ProjetoSocialEscolarService(ProjetoSocialEscolarRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=bool,
    responses={400: {"model": ErrorResponse}},
)
async def create_projeto_social_escolar(
    payload: ProjetoSocialEscolarSave,
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
    return await service.list(page_number=page_number, page_size=page_size)


@router.get(
    "/{codigo_ue}/ue",
    response_model=ProjetoSocialEscolarSchema,
)
async def get_projetos_sociais_por_ue(
    codigo_ue: str,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await service.projetos_sociais_por_ue(codigo_ue)


@router.get(
    "/ue/{ue_id}/existe",
    response_model=bool,
)
async def ue_has_projetos_sociais(
    ue_id: int,
    service: ProjetoSocialEscolarService = Depends(get_service),
):
    return await service.exists_by_ue_id(ue_id)
