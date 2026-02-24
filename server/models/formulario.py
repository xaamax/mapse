from __future__ import annotations

from enum import IntEnum
from typing import Optional

from models.campo import CampoPublic
from sqlmodel import Field, SQLModel, Relationship
from models.base_entity import BaseEntity
from shared.pagination import PaginatedResponse


class Formulario(BaseEntity, table=True):
    __tablename__ = "formularios"

    nome: str = Field(index=True, unique=True)
    slug: str = Field(index=True, unique=True)


class FormularioSchema(SQLModel):
    nome: str
    slug: str


class FormularioPartial(SQLModel):
    nome: Optional[str] = None
    slug: Optional[str] = None
    ativo: Optional[bool] = None


class FormularioPublic(SQLModel):
    id: int
    nome: str
    slug: str

    @classmethod
    def from_model(cls, model: Formulario):
        return cls.model_validate(model)


class FormularioCompact(SQLModel):
    id: int
    nome: str


class FormularioListPaginated(PaginatedResponse[FormularioPublic]):
    pass


class TipoFormularioEnum(IntEnum):
    FORMULARIO_CADASTRO_FORMULARIO = 1

    @property
    def label(self) -> str:
        return {
            TipoFormularioEnum.FORMULARIO_CADASTRO_FORMULARIO:
                "FORMULARIO_CADASTRO_FORMULARIO"
        }[self]


class FormularioDetalhes(SQLModel):
    formulario_id: int
    nome: str
    slug: str
    campos: list[dict]

    @classmethod
    def from_model(cls, model):
        from models.campo import CampoPublic

        campos = [
            CampoPublic.from_model(c).model_dump(exclude={"formulario_id"})
            for c in getattr(model, "campos", [])
        ]
        return cls(**model.__dict__, campos=campos)