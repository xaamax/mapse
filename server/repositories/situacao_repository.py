from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import Situacao


class SituacaoRepository(RepositoryBase[Situacao]):
    def __init__(self, session: Session):
        super().__init__(session, Situacao)
