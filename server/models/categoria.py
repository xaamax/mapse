from typing import Optional

from sqlmodel import Field, SQLModel

from models.base_entity import BaseEntity
from shared.pagination import PaginatedResponse


class Categoria(BaseEntity, table=True):
    __tablename__: str = 'categorias'
    nome: str = Field(index=True, unique=True)


class CategoriaSchema(SQLModel):
    nome: str


class CategoriaPartial(SQLModel):
    nome: Optional[str] = None
    ativo: Optional[bool] = None


class CategoriaPublic(CategoriaSchema):
    id: int
    ativo: bool


class CategoriaCompact(SQLModel):
    id: int
    nome: str


class CategoriaListPaginated(PaginatedResponse[CategoriaPublic]):
    pass
