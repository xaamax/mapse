from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class DreSchema(SQLModel):
    codigo_dre: int
    nome: str
    abreviacao: str
    
class DrePartial(SQLModel):
    nome: Optional[str] = None
    abreviacao: Optional[str] = None
    
class DrePublic(DreSchema):
    codigo_dre: int
    
    
class DreListPaginated(PaginatedResponse[DrePublic]):
    pass