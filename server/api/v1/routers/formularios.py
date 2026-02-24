from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_session
from core.security import get_current_user

from shared.schemas import ErrorResponse

from repositories import FormularioRepository
from models import (
    FormularioCompact,
    FormularioSchema,
    FormularioListPaginated,
    FormularioPartial,
    FormularioPublic,
)
from services import FormularioService

router = APIRouter(dependencies=[Depends(get_current_user)])


def get_service(
    session: AsyncSession = Depends(get_session),
) -> FormularioService:
    return FormularioService(FormularioRepository(session))


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=FormularioPublic,
    responses={400: {"model": ErrorResponse}},
)
async def create_formulario(
    payload: FormularioSchema,
    service: FormularioService = Depends(get_service),
):
    return await service.create(payload)


@router.get(
    "",
    response_model=FormularioListPaginated,
)
async def list_formularios(
    page_number: int = 1,
    page_size: int = 10,
    service: FormularioService = Depends(get_service),
):
    return await service.list(page_number=page_number, page_size=page_size)


@router.get(
    "/opcoes-formularios",
    response_model=list[FormularioCompact],
    responses={404: {"model": ErrorResponse}},
)
async def get_formularios_opcoes(
    service: FormularioService = Depends(get_service),
):
    return await service.opcoes_formulario()


@router.get(
    "/{id}",
    response_model=FormularioSchema,
    responses={404: {"model": ErrorResponse}},
)
async def get_formulario(
    id: int,
    service: FormularioService = Depends(get_service),
):
    return await service.get(id)


@router.get(
    "/{id}/detalhes",
    response_model=dict,
    responses={404: {"model": ErrorResponse}},
)
async def get_formulario_detalhes(
    id: int,
    service: FormularioService = Depends(get_service),
):
    detalhes = await service.detalhes(id)
    return detalhes.model_dump()

@router.put(
    "/{id}",
    response_model=FormularioSchema,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def update_formulario(
    id: int,
    payload: FormularioSchema,
    service: FormularioService = Depends(get_service),
):
    return await service.update(id, payload)


@router.patch(
    "/{id}",
    response_model=FormularioPublic,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
    },
)
async def patch_formulario(
    id: int,
    payload: FormularioPartial,
    service: FormularioService = Depends(get_service),
):
    return await service.patch(id, payload)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": ErrorResponse}},
)
async def delete_formulario(
    id: int,
    service: FormularioService = Depends(get_service),
):
    await service.delete(id)
