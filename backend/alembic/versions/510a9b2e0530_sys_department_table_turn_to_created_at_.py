"""sys_department table turn to created_at updated_at

Revision ID: 510a9b2e0530
Revises: 0c051f553c7f
Create Date: 2024-10-10 03:39:23.141416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '510a9b2e0530'
down_revision: Union[str, None] = '0c051f553c7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sys_department', 'createdAt', new_column_name='created_at')
    op.alter_column('sys_department', 'updatedAt',  new_column_name='updated_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sys_department', 'created_at',  new_column_name='createdAt')
    op.alter_column('sys_department', 'updated_at',  new_column_name='updatedAt')
    # ### end Alembic commands ###