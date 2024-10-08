"""menu table turn to is_show is_cache is_link

Revision ID: bc9fc74fd682
Revises: e0997ddb12c1
Create Date: 2024-10-11 00:02:22.815255

"""
from typing import Sequence, Union

from alembic import op
# import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc9fc74fd682'
down_revision: Union[str, None] = 'e0997ddb12c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sys_menu', 'isShow',  new_column_name='is_show')
    op.alter_column('sys_menu', 'isLink',  new_column_name='is_link')
    op.alter_column('sys_menu', 'isCache',  new_column_name='is_cache')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feed_back', 'is_show',  new_column_name='isShow')
    op.alter_column('feed_back', 'is_link',  new_column_name='isLink')
    op.alter_column('feed_back', 'is_cache',  new_column_name='isCache')
    # ### end Alembic commands ###
