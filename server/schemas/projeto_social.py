from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class ProjetoSocialSchema(SQLModel):
    nome: str
    descricao: str
    endereco: str
    publico_alvo_id: int
    categoria_id: int
    
class ProjetoSocialPartial(SQLModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    endereco: Optional[str] = None
    publico_alvo_id: Optional[int] = None
    categoria_id: Optional[int] = None
    ativo: Optional[bool] = None
    
class ProjetoSocialPublic(SQLModel):
    id: int
    nome: str
    descricao: str
    endereco: str
    categoria_nome: str
    publico_alvo_nome: str
    ativo: bool
    
    @classmethod
    def from_model(cls, model):

        return cls(
            **model.__dict__,
            categoria_nome=model.categoria.nome if model.categoria else None,
            publico_alvo_nome=model.publico_alvo.nome if model.publico_alvo else None,
        )
    
    
class ProjetoSocialListPaginated(PaginatedResponse[ProjetoSocialPublic]):
    pass