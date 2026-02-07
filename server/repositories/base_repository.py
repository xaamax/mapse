from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql import select

from core.utils import get_current_datetime_naive

T = TypeVar('T')


class RepositoryBase(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    async def create(self, model: T) -> T:
        if hasattr(model, 'criado_em') and model.criado_em is None:
            model.criado_em = get_current_datetime_naive()
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model

    def get_by_id(self, entity_id: int) -> T | None:
        return self.session.get(self.model, entity_id)

    async def list(self) -> list[T]:
        result = await self.session.execute(select(T))
        return result.scalars().all()

    async def update(self, model: T) -> T:
        if hasattr(model, 'alterado_em') and model.alterado_em is None:
            model.alterado_em = get_current_datetime_naive()
        await self.session.commit()
        await self.session.refresh(model)
        return model

    async def delete(self, model: T) -> None:
        await self.session.delete(model)
        await self.session.commit()
