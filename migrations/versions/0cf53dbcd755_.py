"""empty message

Revision ID: 0cf53dbcd755
Revises: cf008cb5858c
Create Date: 2021-06-10 22:53:30.786690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf53dbcd755'
down_revision = 'cf008cb5858c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('institution', sa.VARCHAR(), nullable=True))
    op.alter_column('request', 'time_created',
               existing_type=sa.TIME(),
               nullable=True)
    # ### end Alembic commands ###