"""empty message

Revision ID: e9f663477d07
Revises: 2a67e89c40fd
Create Date: 2018-02-15 12:12:03.181066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9f663477d07'
down_revision = '2a67e89c40fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('subject', sa.String(), nullable=False))
    op.drop_column('message', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('message', 'subject')
    # ### end Alembic commands ###
