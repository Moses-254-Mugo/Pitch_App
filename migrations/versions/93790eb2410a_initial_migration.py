"""Initial Migration

Revision ID: 93790eb2410a
Revises: 2e500bbceb48
Create Date: 2021-09-20 00:40:55.350484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93790eb2410a'
down_revision = '2e500bbceb48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
