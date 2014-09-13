"""empty message

Revision ID: 55ac7052999f
Revises: 372c536f4616
Create Date: 2014-08-07 17:23:59.829000

"""

# revision identifiers, used by Alembic.
revision = '55ac7052999f'
down_revision = '372c536f4616'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('author', sa.String(length=255), nullable=True))
    op.add_column('article', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('article', sa.Column('date_created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'date_created')
    op.drop_column('article', 'category')
    op.drop_column('article', 'author')
    ### end Alembic commands ###