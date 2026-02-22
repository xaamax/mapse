from typing import Optional

from sqlmodel import Field, SQLModel

from models.base_entity import BaseEntity
from shared.pagination import PaginatedResponse


class PublicoAlvo(BaseEntity, table=True):
    __tablename__: str = 'publicos_alvos'
    nome: str = Field(index=True, unique=True)


class PublicoAlvoSchema(SQLModel):
    nome: str


class PublicoAlvoPartial(SQLModel):
    nome: Optional[str] = None
    ativo: Optional[bool] = None


class PublicoAlvoPublic(PublicoAlvoSchema):
    id: int
    ativo: bool


class PublicoAlvoCompact(SQLModel):
    id: int
    nome: str


class PublicoAlvoListPaginated(PaginatedResponse[PublicoAlvoPublic]):
    pass
