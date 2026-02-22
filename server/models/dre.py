from typing import Optional

from sqlmodel import Field, SQLModel

from models.base_entity import BaseEntity
from shared.pagination import PaginatedResponse


class Dre(BaseEntity, table=True):
    __tablename__: str = 'dres'
    codigo_dre: str = Field(index=True, unique=True)
    nome: str
    abreviacao: str


class DreSchema(SQLModel):
    codigo_dre: str
    nome: str
    abreviacao: str
    

class DrePartial(SQLModel):
    nome: Optional[str] = None
    ativo: Optional[bool] = None
    abreviacao: Optional[str] = None
    

class DrePublic(DreSchema):
    id: int
    ativo: bool
    
    
class DreCompact(SQLModel):
    codigo_dre: str
    nome: str  
    
    
class DreListPaginated(PaginatedResponse[DrePublic]):
    pass