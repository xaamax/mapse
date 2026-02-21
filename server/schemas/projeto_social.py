from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class ProjetoSocialSchema(SQLModel):
    nome: str
    descricao: str
    endereco: str
    publico_alvo_id: int
    situacao_id: int
    
class ProjetoSocialPartial(SQLModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    endereco: Optional[str] = None
    publico_alvo_id: Optional[int] = None
    situacao_id: Optional[int] = None
    ativo: Optional[bool] = None
    
class ProjetoSocialPublic(ProjetoSocialSchema):
    id: int
    ativo: bool
    
class ProjetoSocialListPaginated(PaginatedResponse[ProjetoSocialPublic]):
    pass