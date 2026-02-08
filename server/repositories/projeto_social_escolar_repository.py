from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import ProjetoSocialEscolar


class ProjetoSocialEscolarRepository(RepositoryBase[ProjetoSocialEscolar]):
    def __init__(self, session: Session):
        super().__init__(session, ProjetoSocialEscolar)