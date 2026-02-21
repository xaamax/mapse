from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field

from models.base_entity import BaseEntity


class ProjetoSocial(BaseEntity, table=True):
    __tablename__: str = 'projetos_sociais'
    nome: str = Field(index=True, unique=True)
    descricao: str
    endereco: str
    publico_alvo_id: int = Field(sa_column=Column(Integer, ForeignKey('publicos_alvos.id', ondelete='CASCADE'), nullable=False))
    situacao_id: int = Field(sa_column=Column(Integer, ForeignKey('situacoes.id', ondelete='CASCADE'), nullable=False))
    

class ProjetoSocialEscolar(BaseEntity, table=True):
    __tablename__: str = 'projetos_sociais_escolares'
    ue_id: int = Field(sa_column=Column(Integer, ForeignKey('ues.id', ondelete='CASCADE'), nullable=False))
    projeto_social_id: int = Field(sa_column=Column(Integer, ForeignKey('projetos_sociais.id', ondelete='CASCADE'), nullable=False))