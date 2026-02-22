from sqlalchemy import select

from core.exceptions import NotFoundException
from sqlalchemy.exc import IntegrityError
from models import ProjetoSocialEscolar
from schemas import ProjetoSocialEscolarSave
from repositories import ProjetoSocialEscolarRepository
from shared.pagination import paginate_response
from models import Ue, Dre


class ProjetoSocialEscolarService:
    def __init__(self, repository: ProjetoSocialEscolarRepository):
        self.repository = repository

    async def _get_or_404(self, id: int) -> ProjetoSocialEscolar:
        model = await self.repository.get_by_id(id)
        if not model:
            raise NotFoundException("Projeto Social Escolar não encontrado")
        return model

    async def create(self, data: ProjetoSocialEscolarSave) -> bool:
        created_any = False
        payload = data.model_dump()
        ue_id = payload.get("ue_id")
        projetos = payload.get("projetos_sociais") or []

        session = self.repository.session

        # obter registros existentes para a UE
        stmt = select(ProjetoSocialEscolar).where(ProjetoSocialEscolar.ue_id == ue_id)
        res = await session.execute(stmt)
        existing_models = res.scalars().all()
        existing_ids = {m.projeto_social_id for m in existing_models}

        new_ids = set(int(x) for x in projetos)

        to_add = new_ids - existing_ids
        to_remove = existing_ids - new_ids

        # adicionar novos
        for projeto_id in to_add:
            model = ProjetoSocialEscolar(ue_id=ue_id, projeto_social_id=projeto_id)
            try:
                await self.repository.create(model)
                created_any = True
            except IntegrityError:
                # se houver condição de corrida, ignore
                continue

        # remover os que não estão mais na lista
        if to_remove:
            for model in existing_models:
                if model.projeto_social_id in to_remove:
                    await self.repository.delete(model)
                    created_any = True

        return created_any

    async def get(self, id: int) -> ProjetoSocialEscolar:
        return await self._get_or_404(id)


    async def list(self, page_number=1, page_size=10):

        query = (
            select(Ue)
            .join(ProjetoSocialEscolar, ProjetoSocialEscolar.ue_id == Ue.id)
            .join(Dre, Ue.dre_id == Dre.id)
            .distinct()
            .order_by(Ue.codigo_ue)
        )

        result = await paginate_response(
            session=self.repository.session,
            query=query,
            page_number=page_number,
            page_size=page_size,
        )

        result["items"] = [
            {
                "codigo_ue": ue.codigo_ue,
                "ue_nome": ue.nome,
                "dre_nome": ue.dre.nome,
            }
            for ue in result["items"]
        ]

        return result


    async def projetos_sociais_por_ue(self, codigo_ue: str) -> dict:
        session = self.repository.session
        stmt = (
            select(
                Ue.id.label("ue_id"),
                Dre.codigo_dre.label("codigo_dre"),
                ProjetoSocialEscolar.projeto_social_id.label("projeto_id"),
            )
            .join(Dre, Ue.dre_id == Dre.id)
            .join(ProjetoSocialEscolar, ProjetoSocialEscolar.ue_id == Ue.id)
            .where(Ue.codigo_ue == codigo_ue)
        )

        result = await session.execute(stmt)
        rows = result.all()
       
        if not rows:
            raise NotFoundException("Nenhum projeto social encontrado para a UE")
        
        ue_id = rows[0].ue_id
        codigo_dre = rows[0].codigo_dre
        projetos = [int(r.projeto_id) for r in rows]

        return {
            "codigo_dre": codigo_dre,
            "ue_id": ue_id,
            "projetos_sociais": projetos,
        }

    async def exists_by_ue_id(self, ue_id: int) -> bool:
        session = self.repository.session
        query = select(ProjetoSocialEscolar.id).where(ProjetoSocialEscolar.ue_id == ue_id).limit(1)
        result = await session.execute(query)
        return result.scalar_one_or_none() is not None
