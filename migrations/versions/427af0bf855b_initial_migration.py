"""Initial Migration

Revision ID: 427af0bf855b
Revises: dcd86ad9ee69
Create Date: 2021-08-18 22:28:56.424831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '427af0bf855b'
down_revision = 'dcd86ad9ee69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitch')
    # ### end Alembic commands ###