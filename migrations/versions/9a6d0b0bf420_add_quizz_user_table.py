"""add quizz user table

Revision ID: 9a6d0b0bf420
Revises: 63e72a394cd1
Create Date: 2023-11-01 20:05:54.608601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a6d0b0bf420'
down_revision = '63e72a394cd1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quizz_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('quizz_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['quizz_id'], ['quizz.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'quizz_id')
    )
    op.drop_column('quizz', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quizz', sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_table('quizz_user')
    # ### end Alembic commands ###
