"""empty message

Revision ID: 1806eaaadac5
Revises: None
Create Date: 2014-08-20 12:03:13.129000

"""

# revision identifiers, used by Alembic.
revision = '1806eaaadac5'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('join_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
