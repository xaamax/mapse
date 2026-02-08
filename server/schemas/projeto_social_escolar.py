from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel

from shared.pagination import PaginatedResponse

class ProjetoSocialEscolarSchema(SQLModel):
    ue_id: int 
    projeto_social_id: int 
    ativo: bool
    
class ProjetoSocialEscolarPartial(SQLModel):
    ue_id: Optional[int] = None
    projeto_social_id: Optional[int] = None
    ativo: Optional[bool] = None
    
class ProjetoSocialEscolarPublic(ProjetoSocialEscolarSchema):
    id: int
    
class ProjetoSocialEscolarListPaginated(PaginatedResponse[ProjetoSocialEscolarPublic]):
    pass