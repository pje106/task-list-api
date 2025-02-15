"""Added bike model

Revision ID: 647dc5256ecc
Revises: 5206a89f6d20
Create Date: 2022-11-07 01:44:59.822546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '647dc5256ecc'
down_revision = '5206a89f6d20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_complete', sa.DateTime(), nullable=True))
    op.drop_column('task', 'completed_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('task', 'is_complete')
    # ### end Alembic commands ###
