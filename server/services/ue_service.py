from core.exceptions import NotFoundException
from models import Ue
from schemas import UeSchema, UePartial
from repositories import UeRepository


class UeService:
    def __init__(self, repository: UeRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> Ue:
        ue = await self.repository.get_by_id(id)
        if not ue:
            raise NotFoundException("UE não encontrada")
        return ue

    async def create(self, data: UeSchema) -> Ue:
        ue = Ue(**data.model_dump())
        return await self.repository.create(ue)

    async def get(self, id: int) -> Ue:
        return await self._get_or_404(id)

    async def update(self, id: int, data: UeSchema) -> Ue:
        ue = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(ue, attr, value)
        return await self.repository.update(ue)

    async def patch(self, id: int, data: UePartial) -> Ue:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        ue = await self._get_or_404(id)
        await self.repository.delete(ue)
