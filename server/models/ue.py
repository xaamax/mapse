from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field, Relationship

from models.base_entity import BaseEntity
from models.dre import Dre


class Ue(BaseEntity, table=True):
    __tablename__: str = 'ues'
    codigo_ue: str = Field(index=True, unique=True)
    nome: str
    endereco: str
    dre_id: int = Field(sa_column=Column(Integer, ForeignKey('dres.id', ondelete='CASCADE'), nullable=False))
    
    dre: Dre | None = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"}
    )