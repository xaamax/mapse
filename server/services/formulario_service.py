from shared.pagination import paginate_response
from sqlalchemy import select

from core.exceptions import NotFoundException
from models import (
    Formulario,
    FormularioPartial,
    FormularioPublic,
    FormularioDetalhes,
    Campo,
    CampoPublic,
)
from repositories import FormularioRepository


class FormularioService:
    def __init__(self, repository: FormularioRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> Formulario:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Formulario não encontrada")
        return model

    async def create(self, data: Formulario) -> Formulario:
        model = Formulario(**data.model_dump())
        return await self.repository.create(model)

    async def get(self, id: int) -> Formulario:
        return await self._get_or_404(id)

    async def update(self, id: int, data: Formulario) -> Formulario:
        model = await self._get_or_404(id)
        for attr, value in data.model_dump().items():
            setattr(model, attr, value)
        return await self.repository.update(model)

    async def patch(self, id: int, data: FormularioPartial) -> Formulario:
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
            query=select(Formulario).order_by(Formulario.id),
            page_number=page_number,
            page_size=page_size,
        )

        result["items"] = [
            FormularioPublic.from_model(x)
            for x in result["items"]
        ]

        return result
    
    
    async def opcoes_formulario(self):
        query = select(Formulario.id, Formulario.nome)
        result = await self.repository.session.execute(query)
        return result.mappings().all()


    async def detalhes(self, id: int) -> FormularioDetalhes:
        model = await self._get_or_404(id)

        query = select(Campo).where(Campo.formulario_id == id).order_by(Campo.ordem)
        result = await self.repository.session.execute(query)
        campos = result.scalars().all()

        campos_public = [
            CampoPublic.from_model(c).model_dump(exclude={"formulario_id"})
            for c in campos
        ]

        return FormularioDetalhes(formulario_id=model.id, nome=model.nome, slug=model.slug, campos=campos_public)