from sqlmodel import Field
from models.base_entity import BaseEntity


class Situacao(BaseEntity, table=True):
    __tablename__: str = 'situacoes'
    nome: str = Field(index=True, unique=True)
