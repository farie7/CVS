"""empty message

Revision ID: f8e0d9b08ead
Revises: 26f0c3bd75f3
Create Date: 2021-06-18 11:40:37.867528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8e0d9b08ead'
down_revision = '26f0c3bd75f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('request', 'time_created',
               existing_type=sa.TIME(),
               nullable=False)
    op.drop_column('request', 'institution')
    op.create_unique_constraint(None, 'request_status', ['student'])
    op.create_unique_constraint(None, 'request_status', ['token_id'])
    op.drop_column('request_status', 'confirmed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request_status', sa.Column('confirmed', sa.BOOLEAN(), nullable=True))
    op.drop_constraint(None, 'request_status', type_='unique')
    op.drop_constraint(None, 'request_status', type_='unique')
    op.add_column('request', sa.Column('institution', sa.VARCHAR(), nullable=True))
    op.alter_column('request', 'time_created',
               existing_type=sa.TIME(),
               nullable=True)
    # ### end Alembic commands ###
