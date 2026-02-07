from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import Ue


class UeRepository(RepositoryBase[Ue]):
    def __init__(self, session: Session):
        super().__init__(session, Ue)
        
    async def get_by_codigo_ue(self, codigo_ue: int) -> Ue | None:
        return await self.get_by_id(
            value=codigo_ue,
            pk_column=Ue.codigo_ue,
        )