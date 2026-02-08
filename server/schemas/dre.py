from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class DreSchema(SQLModel):
    codigo_dre: str
    nome: str
    ativo: bool
    abreviacao: str
    
class DrePartial(SQLModel):
    nome: Optional[str] = None
    ativo: Optional[bool] = None
    abreviacao: Optional[str] = None
    
class DrePublic(DreSchema):
    id: int
    
    
class DreListPaginated(PaginatedResponse[DrePublic]):
    pass