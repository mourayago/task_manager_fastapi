"""inclusão do updated_at na Users

Revision ID: 755aefc6561e
Revises: b3261fed938a
Create Date: 2024-09-25 16:26:16.906517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '755aefc6561e'
down_revision: Union[str, None] = 'b3261fed938a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_column('users', 'updated_at')
    pass
    # ### end Alembic commands ###
