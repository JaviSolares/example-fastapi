"""Add content column to posts table

Revision ID: b7d337897fd0
Revises: 6c7a841a63db
Create Date: 2022-02-23 17:47:44.859684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d337897fd0'
down_revision = '6c7a841a63db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
