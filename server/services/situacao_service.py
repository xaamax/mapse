from sqlalchemy import select

from core.exceptions import NotFoundException
from models import Situacao
from schemas import SituacaoSchema, SituacaoPartial
from repositories import SituacaoRepository


class SituacaoService:
    def __init__(self, repository: SituacaoRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> Situacao:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Situação não encontrada")
        return model

    async def create(self, data: SituacaoSchema) -> Situacao:
        model = Situacao(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> Situacao:
        return await self._get_or_404(id)

    async def update(self, id: int, data: SituacaoSchema) -> Situacao:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: SituacaoPartial) -> Situacao:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)

    async def listar_situacoes(self) -> list[dict]:
        query = select(Situacao.id, Situacao.nome)
        result = await self.repository.session.execute(query)
        return result.mappings().all()