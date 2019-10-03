"""empty message

Revision ID: 1ab5c0ae0407
Revises: 26abac68da5f
Create Date: 2019-10-03 20:42:24.182626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ab5c0ae0407'
down_revision = '26abac68da5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('link_token', sa.String(length=20), nullable=True))
    op.create_unique_constraint(None, 'book', ['link_token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='unique')
    op.drop_column('book', 'link_token')
    # ### end Alembic commands ###
