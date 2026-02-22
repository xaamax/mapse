from core.security import get_password_hash
from models import Usuario
from repositories import UsuarioRepository
from models import UsuarioSchema


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def create(self, data: UsuarioSchema) -> Usuario:
        usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=get_password_hash(data.senha),
        )
        return await self.repository.create(usuario)

    async def get_by_email(self, email: str) -> Usuario | None:
        return await self.repository.get_by_email(email)
