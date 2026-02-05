from typing import Optional

from sqlmodel import Field, SQLModel


class Dre(SQLModel, table=True):
    __tablename__: str = 'dres'
    codigo_dre: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    abreviacao: str