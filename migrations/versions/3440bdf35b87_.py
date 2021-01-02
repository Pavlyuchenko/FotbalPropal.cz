"""empty message

Revision ID: 3440bdf35b87
Revises: 496ae19c1ffe
Create Date: 2021-01-02 13:41:30.597800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3440bdf35b87'
down_revision = '496ae19c1ffe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email_confirmed', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('five_digit', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'five_digit')
    op.drop_column('user', 'email_confirmed')
    # ### end Alembic commands ###