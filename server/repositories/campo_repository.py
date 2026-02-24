from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import Campo


class CampoRepository(RepositoryBase[Campo]):
    def __init__(self, session: Session):
        super().__init__(session, Campo)
