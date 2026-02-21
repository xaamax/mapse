from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse


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
