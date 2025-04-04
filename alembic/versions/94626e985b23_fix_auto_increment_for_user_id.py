"""Fix auto-increment for user_id

Revision ID: 94626e985b23
Revises: e4d2c470fcde
Create Date: 2025-04-04 19:35:14.805610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94626e985b23'
down_revision: Union[str, None] = 'e4d2c470fcde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_registered_users_id'), 'registered_users', ['id'], unique=False)
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_registered_users_id'), table_name='registered_users')
    # ### end Alembic commands ###
