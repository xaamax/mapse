from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse


class SituacaoSchema(SQLModel):
    nome: str


class SituacaoPartial(SQLModel):
    nome: Optional[str] = None
    ativo: Optional[bool] = None


class SituacaoPublic(SituacaoSchema):
    id: int
    ativo: bool


class SituacaoCompact(SQLModel):
    id: int
    nome: str

class SituacaoListPaginated(PaginatedResponse[SituacaoPublic]):
    pass
