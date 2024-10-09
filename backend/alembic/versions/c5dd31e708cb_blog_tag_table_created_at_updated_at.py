"""blog_tag table created_at updated_at

Revision ID: c5dd31e708cb
Revises: 9d3dc66cffc7
Create Date: 2024-10-10 00:16:17.582038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5dd31e708cb'
down_revision: Union[str, None] = '9d3dc66cffc7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_tag', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('blog_tag', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_tag', 'updated_at')
    op.drop_column('blog_tag', 'created_at')
    # ### end Alembic commands ###
