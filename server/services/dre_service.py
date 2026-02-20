from core.exceptions import NotFoundException
from models import Dre
from sqlalchemy import select
from schemas import DreSchema, DrePartial
from repositories import DreRepository


class DreService:
    def __init__(self, repository: DreRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> Dre:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("DRE não encontrada")
        return model

    async def create(self, data: DreSchema) -> Dre:
        model = Dre(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> Dre:
        return await self._get_or_404(id)

    async def update(self, id: int, data: DreSchema) -> Dre:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: DrePartial) -> Dre:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)

    async def listar_codigo_dre_nome(self) -> list[dict]:
        query = select(Dre.codigo_dre, Dre.nome)
        result = await self.repository.session.execute(query)
        return result.mappings().all()
