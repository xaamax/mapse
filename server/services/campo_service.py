from shared.pagination import paginate_response
from sqlalchemy import select

from core.exceptions import NotFoundException
from models import Campo, CampoPartial, CampoPublic, Formulario
from repositories import CampoRepository


class CampoService:
    def __init__(self, repository: CampoRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> Campo:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Campo não encontrado")
        return model

    async def create(self, data: Campo) -> Campo:
        model = Campo(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> Campo:
        return await self._get_or_404(id)

    async def update(self, id: int, data: Campo) -> Campo:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: CampoPartial) -> Campo:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)

    async def list(self, page_number=1, page_size=10):

        result = await paginate_response(
            session=self.repository.session,
            query=select(Campo).order_by(Campo.id),
            page_number=page_number,
            page_size=page_size,
        )

        result["items"] = [
            CampoPublic.from_model(x)
            for x in result["items"]
        ]

        return result