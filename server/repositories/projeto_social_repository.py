from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import ProjetoSocial


class ProjetoSocialRepository(RepositoryBase[ProjetoSocial]):
    def __init__(self, session: Session):
        super().__init__(session, ProjetoSocial)