from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.sql import select

T = TypeVar('T')


class RepositoryBase(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    async def create(self, model: T) -> T:
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model

    async def get_by_id(
        self,
        *,
        value,
        pk_column: ColumnElement,
    ) -> T | None:
        result = await self.session.execute(
            select(self.model).where(pk_column == value)
        )
        return result.scalars().first()

    async def list(self) -> list[T]:
        result = await self.session.execute(select(T))
        return result.scalars().all()

    async def update(self, model: T) -> T:
        await self.session.commit()
        await self.session.refresh(model)
        return model

    async def delete(self, model: T) -> None:
        await self.session.delete(model)
        await self.session.commit()
