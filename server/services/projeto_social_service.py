from sqlalchemy import select

from core.exceptions import NotFoundException
from models import ProjetoSocial
from schemas import ProjetoSocialSchema, ProjetoSocialPartial
from repositories import ProjetoSocialRepository
from schemas.projeto_social import ProjetoSocialPublic
from shared.pagination import paginate_response


class ProjetoSocialService:
    def __init__(self, repository: ProjetoSocialRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> ProjetoSocial:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Projeto Social não encontrado")
        return model

    async def create(self, data: ProjetoSocialSchema) -> ProjetoSocialPublic:
        model = ProjetoSocial(**data.model_dump())
        created = await self.repository.create(model)
        return ProjetoSocialPublic.from_model(created)

    async def get(self, id: int) -> ProjetoSocial:
        return await self._get_or_404(id)

    async def update(self, id: int, data: ProjetoSocialSchema) -> ProjetoSocial:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: ProjetoSocialPartial) -> ProjetoSocialPublic:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        updated = await self.repository.update(model)
        return ProjetoSocialPublic.from_model(updated)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)

    async def list(self, page_number=1, page_size=10):

        result = await paginate_response(
            session=self.repository.session,
            query=select(ProjetoSocial),
            page_number=page_number,
            page_size=page_size,
        )

        result["items"] = [
            ProjetoSocialPublic.from_model(x)
            for x in result["items"]
        ]

        return result