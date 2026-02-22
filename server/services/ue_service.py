from core.exceptions import NotFoundException
from models import Ue, Dre
from models import UeSchema, UePartial
from repositories import UeRepository
from sqlalchemy import select


class UeService:
    def __init__(self, repository: UeRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> Ue:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("UE não encontrada")
        return model

    async def create(self, data: UeSchema) -> Ue:
        model = Ue(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> Ue:
        return await self._get_or_404(id)

    async def update(self, id: int, data: UeSchema) -> Ue:
        model = await self._get_or_404(id)
        for attr, valmodel in data.model_dump().items():
            setattr(model, attr, valmodel)
        return await self.repository.update(model)

    async def patch(self, id: int, data: UePartial) -> Ue:
        model = await self._get_or_404(id)
        update_data = data.model_dump(exclude_unset=True)
        for attr, valmodel in update_data.items():
            setattr(model, attr, valmodel)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)
        
    async def get_by_codigo_dre(self, codigo_dre: str) -> list[Ue]:
        query = (
            select(Ue)
            .join(Dre, Ue.dre_id == Dre.id)
            .where(Dre.codigo_dre == codigo_dre)
        )
        result = await self.repository.session.execute(query)
        return result.scalars().all()        
