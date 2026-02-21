from sqlmodel import Field
from models.base_entity import BaseEntity


class Categoria(BaseEntity, table=True):
    __tablename__: str = 'categorias'
    nome: str = Field(index=True, unique=True)
