"""empty message

Revision ID: 8dd8865dd18a
Revises: 
Create Date: 2019-09-26 00:19:44.434667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dd8865dd18a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(precision=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
