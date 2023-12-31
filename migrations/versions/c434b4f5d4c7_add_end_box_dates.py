"""add end box dates

Revision ID: c434b4f5d4c7
Revises: 879e2aaf3dcd
Create Date: 2023-11-12 19:30:58.379633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c434b4f5d4c7'
down_revision = '879e2aaf3dcd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('end_box1', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('end_box2', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('end_box3', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'end_box3')
    op.drop_column('users', 'end_box2')
    op.drop_column('users', 'end_box1')
    # ### end Alembic commands ###
