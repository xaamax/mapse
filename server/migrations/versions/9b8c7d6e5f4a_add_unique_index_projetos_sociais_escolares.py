"""add_unique_index_projetos_sociais_escolares

Revision ID: 9b8c7d6e5f4a
Revises: fbd17311dc6b
Create Date: 2026-02-21 20:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9b8c7d6e5f4a'
down_revision: Union[str, None] = 'fbd17311dc6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # create unique index to prevent duplicate (ue_id, projeto_social_id)
    op.create_index(
        'uq_projetos_sociais_escolares_ue_projeto',
        'projetos_sociais_escolares',
        ['ue_id', 'projeto_social_id'],
        unique=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('uq_projetos_sociais_escolares_ue_projeto', table_name='projetos_sociais_escolares')
