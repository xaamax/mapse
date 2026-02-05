from core.exceptions import NotFoundException
from models import Dre
from schemas import DreSchema, DrePartial
from repositories import DreRepository


class DreService:
    def __init__(self, repository: DreRepository):
        self.repository = repository

    async def _get_or_404(self, codigo_dre: int) -> Dre:
        dre = await self.repository.get_by_codigo_dre(codigo_dre)
        if not dre:
            raise NotFoundException("DRE não encontrada")
        return dre

    async def create(self, data: DreSchema) -> Dre:
        dre = Dre(**data.model_dump())
        return await self.repository.create(dre)

    async def get(self, codigo_dre: int) -> Dre:
        return await self._get_or_404(codigo_dre)

    async def update(self, codigo_dre: int, data: DreSchema) -> Dre:
        dre = await self._get_or_404(codigo_dre)
        for attr, value in data.model_dump().items():
            setattr(dre, attr, value)
        return await self.repository.update(dre)

    async def patch(self, codigo_dre: int, data: DrePartial) -> Dre:
        model = await self._get_or_404(codigo_dre)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, codigo_dre: int) -> None:
        dre = await self._get_or_404(codigo_dre)
        await self.repository.delete(dre)
