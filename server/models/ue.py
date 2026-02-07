from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field

from models.base_entity import BaseEntity


class Ue(BaseEntity, table=True):
    __tablename__: str = 'ues'
    codigo_ue: str = Field(index=True, unique=True)
    nome: str
    endereco: str
    dre_id: int = Field(sa_column=Column(Integer, ForeignKey('dres.id', ondelete='CASCADE'), nullable=False))