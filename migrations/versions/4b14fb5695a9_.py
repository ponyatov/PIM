"""empty message

Revision ID: 4b14fb5695a9
Revises: fd54e26c4963
Create Date: 2018-10-10 17:17:46.037974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b14fb5695a9'
down_revision = 'fd54e26c4963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('login', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('pwdhash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_login'), 'user', ['login'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_login'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'pwdhash')
    op.drop_column('user', 'login')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
