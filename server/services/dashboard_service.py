from sqlalchemy import select, func

from repositories.dashboard_repository import DashboardRepository

from models import (
    ProjetoSocial,
    Categoria,
    PublicoAlvo,
    Ue,
    Dre,
    ProjetoSocialEscolar,
)


class DashboardService:
    def __init__(self, repository: DashboardRepository):
        self.repo = repository

    async def get_dashboard(self) -> dict:
        session = self.repo.session

        r = await session.execute(select(func.count(ProjetoSocial.id)))
        projetos_count = int(r.scalar_one() or 0)

        r = await session.execute(select(func.count(Categoria.id)))
        categorias_count = int(r.scalar_one() or 0)

        r = await session.execute(select(func.count(PublicoAlvo.id)))
        publicos_count = int(r.scalar_one() or 0)

        r = await session.execute(select(func.count(ProjetoSocialEscolar.ue_id.distinct())))
        ues_atendidas_count = int(r.scalar_one() or 0)

        q = (
            select(Categoria.nome.label("label"), func.count(ProjetoSocial.id).label("total"))
            .join(ProjetoSocial, ProjetoSocial.categoria_id == Categoria.id)
            .group_by(Categoria.nome)
            .order_by(func.count(ProjetoSocial.id).desc())
        )
        res = await session.execute(q)
        projetos_por_categoria = [dict(label=row.label, total=int(row.total)) for row in res.all()]

        q = (
            select(Dre.nome.label("dre_nome"), Dre.abreviacao.label("dre_sigla"), func.count(ProjetoSocialEscolar.ue_id.distinct()).label("total_ues"), func.count(ProjetoSocialEscolar.ue_id).label("total_projetos_escolares"))
            .join(Ue, Ue.dre_id == Dre.id)
            .join(ProjetoSocialEscolar, ProjetoSocialEscolar.ue_id == Ue.id)
            .group_by(Dre.nome, Dre.abreviacao)
            .order_by(func.count(ProjetoSocialEscolar.ue_id.distinct()).desc())
        )
        res = await session.execute(q)
        projetos_por_dre = [dict(dre_nome=row.dre_nome.split('DIRETORIA REGIONAL DE EDUCACAO ')[1], dre_sigla=row.dre_sigla.split(' - ')[1], total_ues=int(row.total_ues), total_projetos_escolares=int(row.total_projetos_escolares)) for row in res.all()]

        q = (
            select(PublicoAlvo.nome.label("label"), func.count(ProjetoSocial.id).label("total"))
            .join(ProjetoSocial, ProjetoSocial.publico_alvo_id == PublicoAlvo.id)
            .group_by(PublicoAlvo.nome)
            .order_by(func.count(ProjetoSocial.id).desc())
        )
        res = await session.execute(q)
        projetos_por_publico = [dict(label=row.label, total=int(row.total)) for row in res.all()]

        return {
            "indicadores": [
                {"title": "Projetos Sociais", "value": projetos_count, "icon": "FolderOpen"},
                {"title": "Unidades Educacionais Atendidas", "value": ues_atendidas_count, "icon": "Building"},
                {"title": "Categorias", "value": categorias_count, "icon": "Tag"},
                {"title": "Públicos Alvos", "value": publicos_count, "icon": "Users"},
            ],
            "projetos_sociais_categoria": projetos_por_categoria,
            "projetos_sociais_dre": projetos_por_dre,
            "projetos_sociais_publico_alvo": projetos_por_publico,
        }
