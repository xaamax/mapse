from sqlalchemy import select
from sqlalchemy.orm import Session

from .base_repository import RepositoryBase
from models import Usuario


class UsuarioRepository(RepositoryBase[Usuario]):
    def __init__(self, session: Session):
        super().__init__(session, Usuario)

    async def get_by_email(self, email: str) -> Usuario | None:
        result = await self.session.execute(
            select(Usuario).where(Usuario.email == email)
        )
        return result.scalar_one_or_none()
