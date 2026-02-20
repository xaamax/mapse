from sqlmodel import Field

from models.base_entity import BaseEntity


class Usuario(BaseEntity, table=True):
    __tablename__: str = "usuarios"

    nome: str
    email: str = Field(index=True, unique=True)
    senha: str
