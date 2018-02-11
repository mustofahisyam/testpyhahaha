"""empty message

Revision ID: ac58d6c97c93
Revises: 
Create Date: 2017-10-19 00:00:16.014894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac58d6c97c93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('klustermodels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=64), nullable=True),
    sa.Column('active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nama')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vectorspaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nama')
    )
    op.create_table('kelompoks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.Integer(), nullable=True),
    sa.Column('kuncikata', sa.String(length=128), nullable=True),
    sa.Column('warna', sa.String(length=32), nullable=True),
    sa.Column('klustermodel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['klustermodel_id'], ['klustermodels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('cleandatas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pertanyaan', sa.String(length=256), nullable=True),
    sa.Column('data_asli', sa.String(length=256), nullable=True),
    sa.Column('kelompok_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kelompok_id'], ['kelompoks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cleandatas')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('kelompoks')
    op.drop_table('vectorspaces')
    op.drop_table('roles')
    op.drop_table('klustermodels')
    # ### end Alembic commands ###