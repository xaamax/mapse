from typing import Optional

from sqlmodel import SQLModel
from shared.pagination import PaginatedResponse

class UsuarioSchema(SQLModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioSchema):
    senha: str

class UsuarioPartial(SQLModel):
    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]


class UsuarioPublic(UsuarioSchema):
    id: int
    ativo: bool


class UsuarioLogin(SQLModel):
    email: str
    senha: str


class UsuarioListPaginated(PaginatedResponse[UsuarioPublic]):
    pass