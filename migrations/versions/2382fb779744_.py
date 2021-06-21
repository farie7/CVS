"""empty message

Revision ID: 2382fb779744
Revises: e2b2c29f5edb
Create Date: 2021-06-10 13:29:40.028818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2382fb779744'
down_revision = 'e2b2c29f5edb'
branch_labels = None
depends_on = None


def upgrade():
    # # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('request_status', 'user_id',
    #            existing_type=sa.Column(),
    #            nullable=True)
    # op.drop_column('request', 'institution')
    # op.add_column('request_status', sa.Column('user_id', sa.String(), nullable=False))
    # op.add_column('request_status', sa.Column('date_created', sa.Date(), nullable=True))
    # op.add_column('request_status', sa.Column('time_created', sa.String(), nullable=True))
    # ### end Alembic commands ###
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('request_status', 'time_created')
    op.drop_column('request_status', 'date_created')
    op.drop_column('request_status', 'user_id')
    op.add_column('request', sa.Column('institution', sa.VARCHAR(), nullable=True))
    op.alter_column('request', 'time_created',
               existing_type=sa.TIME(),
               nullable=True)
    # ### end Alembic commands ###
