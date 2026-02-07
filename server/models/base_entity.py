from datetime import datetime
from typing import Optional

from sqlalchemy.types import DateTime, TypeDecorator
from sqlmodel import Field, SQLModel


class NaiveDateTime(TypeDecorator):
    """DateTime sem timezone para PostgreSQL"""
    impl = DateTime
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None or not isinstance(value, datetime):
            return value
        return value.replace(tzinfo=None) if value.tzinfo else value


class BaseEntity(SQLModel): 
    id: Optional[int] = Field(default=None, primary_key=True)
    ativo: bool = Field(default=True, index=True)
    criado_em: Optional[datetime] = Field(default=None, sa_type=NaiveDateTime)
    alterado_em: Optional[datetime] = Field(default=None, sa_type=NaiveDateTime)
    excluido_em: Optional[datetime] = Field(default=None, sa_type=NaiveDateTime)
