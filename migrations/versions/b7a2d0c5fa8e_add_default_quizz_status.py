"""add default quizz status

Revision ID: b7a2d0c5fa8e
Revises: c434b4f5d4c7
Create Date: 2023-11-15 17:48:30.361740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7a2d0c5fa8e'
down_revision = 'c434b4f5d4c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quizz', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('quizz', 'status')
    # ### end Alembic commands ###
