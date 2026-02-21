from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import Categoria


class CategoriaRepository(RepositoryBase[Categoria]):
    def __init__(self, session: Session):
        super().__init__(session, Categoria)
