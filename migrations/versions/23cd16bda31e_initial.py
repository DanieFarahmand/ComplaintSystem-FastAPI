"""initial

Revision ID: 23cd16bda31e
Revises: 
Create Date: 2023-06-27 15:07:23.029266

"""
from alembic import op
import sqlalchemy as sa

from models import RoleType, ComplaintState

# revision identifiers, used by Alembic.
revision = '23cd16bda31e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'complaints',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=120), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('photo_url', sa.String(length=200), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('create_date', sa.DateTime(), nullable=True, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('status', sa.Enum(ComplaintState), nullable=False, server_default=ComplaintState.pending.name),
        sa.Column('complainer_id', sa.Integer(), nullable=False),  # Specify the type for complainer_id
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=128), nullable=True),
        sa.Column('firstname', sa.String(length=128), nullable=True),
        sa.Column('lastname', sa.String(length=128), nullable=True),
        sa.Column('password', sa.String(length=128), nullable=True),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('iban', sa.String(length=34), nullable=True),
        sa.Column('role', sa.Enum(RoleType), nullable=False, server_default=RoleType.complainer.name),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('complaints')
