from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class ProjetoSocialEscolarSchema(SQLModel):
    codigo_dre: str
    ue_id: int   
    projetos_sociais: list[int]
    
    
class ProjetoSocialEscolarSave(SQLModel):
    ue_id: int   
    projetos_sociais: list[int]
        
    
class ProjetoSocialEscolarPublic(SQLModel):
    codigo_ue: str
    ue_nome: str
    dre_nome: str
    
    @classmethod
    def from_model(cls, model):
        return cls(
            codigo_ue=model.ue.codigo_ue if model.ue else None,
            ue_nome=model.ue.nome if model.ue else None,
            dre_nome=model.ue.dre.nome if model.ue and model.ue.dre else None
        )
    
    
class ProjetoSocialEscolarListPaginated(PaginatedResponse[ProjetoSocialEscolarPublic]):
    pass