from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class UeSchema(SQLModel):
    codigo_ue: str
    nome: str
    endereco: str
    dre_id: int 
    
class UePartial(SQLModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    ativo: Optional[bool] = None
    dre_id: Optional[int] = None
    
class UePublic(UeSchema):
    id: int
    ativo: bool
    
    
class UeCompact(SQLModel):
    id: int
    codigo_ue: str
    nome: str
    
    
class UeListPaginated(PaginatedResponse[UePublic]):
    pass