"""adds video  model

Revision ID: 68f16c25ebd8
Revises: 50db8e9a2a35
Create Date: 2021-05-18 21:56:22.881659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68f16c25ebd8'
down_revision = '50db8e9a2a35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('available_inventory', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'available_inventory')
    # ### end Alembic commands ###
