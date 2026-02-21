from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field, Relationship

from models.base_entity import BaseEntity
from models.publico_alvo import PublicoAlvo
from models.categoria import Categoria


class ProjetoSocial(BaseEntity, table=True):
    __tablename__: str = 'projetos_sociais'
    nome: str = Field(index=True, unique=True)
    descricao: str
    publico_alvo_id: int = Field(sa_column=Column(Integer, ForeignKey('publicos_alvos.id', ondelete='CASCADE'), nullable=False))
    categoria_id: int = Field(sa_column=Column(Integer, ForeignKey('categorias.id', ondelete='CASCADE'), nullable=False))
    
    publico_alvo: PublicoAlvo | None = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"}
    )

    categoria: Categoria | None = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"}
    )


class ProjetoSocialEscolar(BaseEntity, table=True):
    __tablename__: str = 'projetos_sociais_escolares'
    ue_id: int = Field(sa_column=Column(Integer, ForeignKey('ues.id', ondelete='CASCADE'), nullable=False))
    projeto_social_id: int = Field(sa_column=Column(Integer, ForeignKey('projetos_sociais.id', ondelete='CASCADE'), nullable=False))