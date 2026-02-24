from enum import IntEnum
from typing import Optional
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlmodel import Field, SQLModel

from models.base_entity import BaseEntity
from shared.pagination import PaginatedResponse



class Campo(BaseEntity, table=True):
    __tablename__ = "campos"

    __table_args__ = (
        UniqueConstraint(
            "nome",
            "label",
            "formulario_id",
            name="uq_campo_nome_label_formulario",
        ),
    )

    nome: str
    label: str
    observacao: Optional[str] = Field(default=None, nullable=True)
    ordem: int
    tipo: int
    opcional: Optional[str] = Field(default=None, nullable=True)
    xs: Optional[int] = Field(default=None, nullable=True)
    lg: Optional[int] = Field(default=None, nullable=True)
    md: Optional[int] = Field(default=None, nullable=True)
    sm: Optional[int] = Field(default=None, nullable=True)
    readonly: bool = Field(default=False)
    tamanho: Optional[int] = Field(default=None, nullable=True)
    mascara: Optional[str] = Field(default=None, nullable=True)
    placeholder: Optional[str] = Field(default=None, nullable=True)

    formulario_id: int = Field(
        sa_column=Column(
            Integer,
            ForeignKey("formularios.id", ondelete="CASCADE"),
            nullable=False,
        )
    )


class CampoSchema(SQLModel):
    nome: str
    label: str
    observacao: Optional[str] = None
    ordem: int
    tipo: int
    opcional: Optional[str] = None
    xs: Optional[int] = None
    lg: Optional[int] = None
    md: Optional[int] = None
    sm: Optional[int] = None
    readonly: bool = False
    tamanho: Optional[int] = None
    mascara: Optional[str] = None
    placeholder: Optional[str] = None
    formulario_id: int


class CampoPartial(SQLModel):
    nome: Optional[str] = None
    label: Optional[str] = None
    observacao: Optional[str] = None
    ordem: Optional[int] = None
    tipo: Optional[int] = None
    opcional: Optional[str] = None
    xs: Optional[int] = None
    lg: Optional[int] = None
    md: Optional[int] = None
    sm: Optional[int] = None
    readonly: Optional[bool] = None
    tamanho: Optional[int] = None
    mascara: Optional[str] = None
    placeholder: Optional[str] = None
    formulario_id: Optional[int] = None


class CampoPublic(SQLModel):
    id: int
    nome: str
    label: str
    observacao: Optional[str] = None
    ordem: int
    tipo: int
    tipo_campo: Optional[str] = None
    opcional: Optional[str] = None
    xs: Optional[int] = None
    lg: Optional[int] = None
    md: Optional[int] = None
    sm: Optional[int] = None
    readonly: bool = False
    tamanho: Optional[int] = None
    mascara: Optional[str] = None
    placeholder: Optional[str] = None
    formulario_id: int

    @classmethod
    def from_model(cls, model: Campo):
        data = {
            **model.model_dump(),
            'tipo_campo': (
                TipoCampoEnum(model.tipo).label
                if model.tipo is not None
                else None
            ),
        }
        return cls.model_validate(data)


class CampoListPaginated(PaginatedResponse[CampoPublic]):
    pass


class TipoCampoEnum(IntEnum):
    FRASE = 1
    TEXTO = 2
    NUMERICO = 3
    DATA = 4
    RADIO = 5
    SELECT = 6
    CHECKBOX = 7
    UPLOAD = 8

    @property
    def label(self) -> str:
        labels = {
            TipoCampoEnum.FRASE: 'FRASE',
            TipoCampoEnum.TEXTO: 'TEXTO',
            TipoCampoEnum.NUMERICO: 'NUMERICO',
            TipoCampoEnum.DATA: 'DATA',
            TipoCampoEnum.RADIO: 'RADIO',
            TipoCampoEnum.SELECT: 'SELECT',
            TipoCampoEnum.CHECKBOX: 'CHECKBOX',
            TipoCampoEnum.UPLOAD: 'UPLOAD',
        }
        return labels[self]