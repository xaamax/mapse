from sqlalchemy.orm import Session

from .base_repository import RepositoryBase

from models import Dre


class DreRepository(RepositoryBase[Dre]):
    def __init__(self, session: Session):
        super().__init__(session, Dre)
        
    async def get_by_codigo_dre(self, codigo_dre: int) -> Dre | None:
        return await self.get_by_id(
            value=codigo_dre,
            pk_column=Dre.codigo_dre,
        )