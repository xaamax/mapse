from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import PublicoAlvo


class PublicoAlvoRepository(RepositoryBase[PublicoAlvo]):
    def __init__(self, session: Session):
        super().__init__(session, PublicoAlvo)
