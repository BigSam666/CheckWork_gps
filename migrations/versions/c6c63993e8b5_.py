"""empty message

Revision ID: c6c63993e8b5
Revises: 50e36156c3bd
Create Date: 2018-03-01 14:07:09.692216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6c63993e8b5'
down_revision = '50e36156c3bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check_work', sa.Column('test', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('check_work', 'test')
    # ### end Alembic commands ###
