"""sys user table turn to created_at updated_at

Revision ID: c351184a87a2
Revises: 622d6ce1333d
Create Date: 2024-10-10 03:02:28.077336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c351184a87a2'
down_revision: Union[str, None] = '622d6ce1333d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sys_user', 'createdAt', new_column_name='created_at')
    op.alter_column('sys_user', 'updatedAt',  new_column_name='updated_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sys_user', 'created_at',  new_column_name='createdAt')
    op.alter_column('sys_user', 'updated_at',  new_column_name='updatedAt')
    # ### end Alembic commands ###
