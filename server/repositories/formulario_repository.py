from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import Formulario


class FormularioRepository(RepositoryBase[Formulario]):
    def __init__(self, session: Session):
        super().__init__(session, Formulario)
