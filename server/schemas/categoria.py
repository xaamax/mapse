from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse


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
