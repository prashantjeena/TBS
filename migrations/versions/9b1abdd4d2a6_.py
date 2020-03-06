"""empty message

Revision ID: 9b1abdd4d2a6
Revises: 5ad50daed834
Create Date: 2019-10-20 10:19:30.313115

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b1abdd4d2a6'
down_revision = '5ad50daed834'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audi', sa.Column('theatre_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'audi', 'theatre', ['theatre_id'], ['id'])
    op.add_column('movie', sa.Column('theatre_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'movie', 'theatre', ['theatre_id'], ['id'])
    op.drop_constraint('theatre_ibfk_1', 'theatre', type_='foreignkey')
    op.drop_constraint('theatre_ibfk_2', 'theatre', type_='foreignkey')
    op.drop_column('theatre', 'movie_id')
    op.drop_column('theatre', 'audi_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('theatre', sa.Column('audi_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('theatre', sa.Column('movie_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('theatre_ibfk_2', 'theatre', 'movie', ['movie_id'], ['id'])
    op.create_foreign_key('theatre_ibfk_1', 'theatre', 'audi', ['audi_id'], ['id'])
    op.drop_constraint(None, 'movie', type_='foreignkey')
    op.drop_column('movie', 'theatre_id')
    op.drop_constraint(None, 'audi', type_='foreignkey')
    op.drop_column('audi', 'theatre_id')
    # ### end Alembic commands ###
