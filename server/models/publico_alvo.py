from sqlmodel import Field
from models.base_entity import BaseEntity


class PublicoAlvo(BaseEntity, table=True):
    __tablename__: str = 'publicos_alvos'
    nome: str = Field(index=True, unique=True)
