"""review objective model

Revision ID: 3b27c106103b
Revises: 311910cb7c37
Create Date: 2023-11-01 15:53:24.694773

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3b27c106103b'
down_revision = '311910cb7c37'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request_character_user')
    op.add_column('objective', sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.drop_column('objective', 'status')
    op.drop_column('objective', 'subtitle')
    op.drop_column('objective', 'title')
    op.drop_column('objective', 'detail')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objective', sa.Column('detail', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('objective', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('objective', sa.Column('subtitle', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('objective', sa.Column('status', postgresql.ENUM('open', 'closed', 'done', name='objectivestatus'), autoincrement=False, nullable=True))
    op.drop_column('objective', 'data')
    op.create_table('request_character_user',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('request_character_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ref_data', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['request_character_id'], ['request_character.id'], name='request_character_user_request_character_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='request_character_user_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'request_character_id', name='request_character_user_pkey')
    )
    # ### end Alembic commands ###
