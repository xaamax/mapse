from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class ProjetoSocialSchema(SQLModel):
    nome: str
    descricao: str
    endereco: str
    publico_alvo: int 
    situacao: int 
    ue_id: int 
    
class ProjetoSocialPartial(SQLModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    endereco: Optional[str] = None
    publico_alvo: Optional[int] = None
    situacao: Optional[int] = None
    ativo: Optional[bool] = None
    ue_id: Optional[int] = None
    
class ProjetoSocialPublic(ProjetoSocialSchema):
    id: int
    ativo: bool
    
class ProjetoSocialListPaginated(PaginatedResponse[ProjetoSocialPublic]):
    pass