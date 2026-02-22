from sqlalchemy import select

from core.exceptions import NotFoundException
from models import PublicoAlvo
from models import PublicoAlvoSchema, PublicoAlvoPartial
from repositories import PublicoAlvoRepository


class PublicoAlvoService:
    def __init__(self, repository: PublicoAlvoRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> PublicoAlvo:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Público alvo não encontrado")
        return model

    async def create(self, data: PublicoAlvoSchema) -> PublicoAlvo:
        model = PublicoAlvo(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> PublicoAlvo:
        return await self._get_or_404(id)

    async def update(self, id: int, data: PublicoAlvoSchema) -> PublicoAlvo:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: PublicoAlvoPartial) -> PublicoAlvo:
        model = await self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)
        for attr, value in update_data.items():
            setattr(model, attr, value)

        return await self.repository.update(model)

    async def delete(self, id: int) -> None:
        model = await self._get_or_404(id)
        await self.repository.delete(model)

    async def listar_publicos_alvos(self) -> list[dict]:
        query = select(PublicoAlvo.id, PublicoAlvo.nome).order_by(PublicoAlvo.id)
        result = await self.repository.session.execute(query)
        return result.mappings().all()