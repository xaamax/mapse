from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field, Relationship, SQLModel

from models.base_entity import BaseEntity
from models.dre import Dre
from shared.pagination import PaginatedResponse


class Ue(BaseEntity, table=True):
    __tablename__: str = 'ues'
    codigo_ue: str = Field(index=True, unique=True)
    nome: str
    endereco: str
    dre_id: int = Field(sa_column=Column(Integer, ForeignKey('dres.id', ondelete='CASCADE'), nullable=False))
    
    dre: Dre | None = Relationship(
        sa_relationship_kwargs={"lazy": "selectin"}
    )


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