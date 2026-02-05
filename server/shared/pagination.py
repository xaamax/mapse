from typing import Generic, List, TypeVar
from pydantic import BaseModel

from sqlalchemy import func, select
from sqlalchemy.sql import Select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    page_number: int
    page_size: int
    total_items: int


async def paginate_response(
    *,
    session: AsyncSession,
    query: Select,
    page_number: int,
    page_size: int,
) -> dict:
    page_number = max(page_number, 1)
    page_size = max(page_size, 1)

    offset = (page_number - 1) * page_size

    total_items = (
        await session.execute(
            select(func.count()).select_from(query.subquery())
        )
    ).scalar_one()

    items = (
        await session.execute(
            query.offset(offset).limit(page_size)
        )
    ).scalars().all()

    return {
        "items": items,
        "page_number": page_number,
        "page_size": page_size,
        "total_items": total_items,
    }