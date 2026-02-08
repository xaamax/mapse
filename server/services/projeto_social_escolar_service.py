from core.exceptions import NotFoundException
from models import ProjetoSocialEscolar
from schemas import ProjetoSocialEscolarSchema, ProjetoSocialEscolarPartial
from repositories import ProjetoSocialEscolarRepository


class ProjetoSocialEscolarService:
    def __init__(self, repository: ProjetoSocialEscolarRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> ProjetoSocialEscolar:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Projeto Social Escolar não encontrado")
        return model

    async def create(self, data: ProjetoSocialEscolarSchema) -> ProjetoSocialEscolar:
        model = ProjetoSocialEscolar(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> ProjetoSocialEscolar:
        return await self._get_or_404(id)

    async def update(self, id: int, data: ProjetoSocialEscolarSchema) -> ProjetoSocialEscolar:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: ProjetoSocialEscolarPartial) -> ProjetoSocialEscolar:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)
