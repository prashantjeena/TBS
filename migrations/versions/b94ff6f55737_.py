"""empty message

Revision ID: b94ff6f55737
Revises: 86beae9323e1
Create Date: 2019-10-23 23:15:58.413014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b94ff6f55737'
down_revision = '86beae9323e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('public_id', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'movie', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'movie', type_='unique')
    op.drop_column('movie', 'public_id')
    # ### end Alembic commands ###
