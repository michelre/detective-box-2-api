"""add quizz and help tables

Revision ID: 4ee187cc25db
Revises: 822b27d3bebd
Create Date: 2023-10-22 22:55:52.927722

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4ee187cc25db'
down_revision = '822b27d3bebd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('help',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('open', 'closed', 'done', name='helpstatus'), nullable=True),
    sa.Column('box_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['box_id'], ['box.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_help_id'), 'help', ['id'], unique=False)
    op.create_table('quizz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('choices', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('image_question', sa.String(), nullable=True),
    sa.Column('answer', sa.Text(), nullable=True),
    sa.Column('explanation', sa.Text(), nullable=True),
    sa.Column('image_answer', sa.String(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('box_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['box_id'], ['box.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quizz_id'), 'quizz', ['id'], unique=False)
    op.create_table('hint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('help_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['help_id'], ['help.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hint_id'), 'hint', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hint_id'), table_name='hint')
    op.drop_table('hint')
    op.drop_index(op.f('ix_quizz_id'), table_name='quizz')
    op.drop_table('quizz')
    op.drop_index(op.f('ix_help_id'), table_name='help')
    op.drop_table('help')
    sa.Enum('open', 'closed', 'done', name='helpstatus').drop(op.get_bind())
    # ### end Alembic commands ###