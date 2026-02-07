from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class UeSchema(SQLModel):
    codigo_ue: str
    nome: str
    endereco: str
    ativo: bool
    dre_id: int 
    
class UePartial(SQLModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    ativo: Optional[bool] = None
    dre_id: Optional[int] = None
    
class UePublic(UeSchema):
    id: int
    ativo: bool
    criado_em: datetime
    alterado_em: Optional[datetime] = None
    excluido_em: Optional[datetime] = None
    
    
class UeListPaginated(PaginatedResponse[UePublic]):
    pass