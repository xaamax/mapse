from sqlmodel import Field

from models.base_entity import BaseEntity


class Dre(BaseEntity, table=True):
    __tablename__: str = 'dres'
    codigo_dre: str = Field(index=True, unique=True)
    nome: str
    abreviacao: str