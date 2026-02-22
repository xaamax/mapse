from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field, Relationship, SQLModel

from typing import Optional

from models.base_entity import BaseEntity
from models.publico_alvo import PublicoAlvo
from models.categoria import Categoria
from models.ue import Ue
from shared.pagination import PaginatedResponse


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


class ProjetoSocialEscolar(SQLModel, table=True):
    __tablename__: str = 'projetos_sociais_escolares'
    id: int = Field(default=None, primary_key=True)
    ue_id: int = Field(sa_column=Column(Integer, ForeignKey('ues.id', ondelete='CASCADE'), nullable=False))
    projeto_social_id: int = Field(sa_column=Column(Integer, ForeignKey('projetos_sociais.id', ondelete='CASCADE'), nullable=False))
    
    ue: Ue | None = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"}
    )
    
    projeto_social: ProjetoSocial | None = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"}
    )


class ProjetoSocialSchema(SQLModel):
    nome: str
    descricao: str
    publico_alvo_id: int
    categoria_id: int
    

class ProjetoSocialPartial(SQLModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    publico_alvo_id: Optional[int] = None
    categoria_id: Optional[int] = None
    ativo: Optional[bool] = None
    

class ProjetoSocialPublic(SQLModel):
    id: int
    nome: str
    descricao: str
    categoria_nome: str
    publico_alvo_nome: str
    ativo: bool
    
    @classmethod
    def from_model(cls, model):

        return cls(
            **model.__dict__,
            categoria_nome=model.categoria.nome if model.categoria else None,
            publico_alvo_nome=model.publico_alvo.nome if model.publico_alvo else None,
        )
    
    
class ProjetoSocialListPaginated(PaginatedResponse[ProjetoSocialPublic]):
    pass


class ProjetoSocialEscolarSchema(SQLModel):
    codigo_dre: str
    ue_id: int   
    projetos_sociais: list[int]
    

class ProjetoSocialEscolarSave(SQLModel):
    ue_id: int   
    projetos_sociais: list[int]
        


class ProjetoSocialEscolarPublic(SQLModel):
    codigo_ue: str
    ue_nome: str
    dre_nome: str
    
    @classmethod
    def from_model(cls, model):
        return cls(
            codigo_ue=model.ue.codigo_ue if model.ue else None,
            ue_nome=model.ue.nome if model.ue else None,
            dre_nome=model.ue.dre.nome if model.ue and model.ue.dre else None
        )
    
    
class ProjetoSocialEscolarListPaginated(PaginatedResponse[ProjetoSocialEscolarPublic]):
    pass