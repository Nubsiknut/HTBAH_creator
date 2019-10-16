"""empty message

Revision ID: f66292353f12
Revises: f4cf3d89d7aa
Create Date: 2019-10-16 23:54:57.115401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f66292353f12'
down_revision = 'f4cf3d89d7aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charactersheet', sa.Column('User', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'charactersheet', type_='foreignkey')
    op.create_foreign_key(None, 'charactersheet', 'user', ['User'], ['id'])
    op.drop_column('charactersheet', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charactersheet', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'charactersheet', type_='foreignkey')
    op.create_foreign_key(None, 'charactersheet', 'user', ['user_id'], ['id'])
    op.drop_column('charactersheet', 'User')
    # ### end Alembic commands ###