from typing import Optional

from sqlmodel import Field, SQLModel

from models.base_entity import BaseEntity
from shared.pagination import PaginatedResponse


class Usuario(BaseEntity, table=True):
    __tablename__: str = "usuarios"

    nome: str
    email: str = Field(index=True, unique=True)
    senha: str


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
