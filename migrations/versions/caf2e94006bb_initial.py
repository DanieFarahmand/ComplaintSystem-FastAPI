"""Initial

Revision ID: caf2e94006bb
Revises: 
Create Date: 2023-06-24 16:58:13.290808

"""
from alembic import op
import sqlalchemy as sa

from models import RoleType, ComplaintState

# revision identifiers, used by Alembic.
revision = 'caf2e94006bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(128), unique=True),
        sa.Column('username', sa.String(128), unique=True),
        sa.Column('firstname', sa.String(128)),
        sa.Column('lastname', sa.String(128)),
        sa.Column('iban', sa.String(34)),
        sa.Column('role', sa.Enum(RoleType), nullable=False,
                  server_default=RoleType.complainer.name),
    )

    # Create the complaints table
    op.create_table(
        'complaints',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(120), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('photo_url', sa.String(200), nullable=False),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('create_date', sa.DateTime, server_default=sa.func.now()),
        sa.Column('status', sa.Enum(ComplaintState), nullable=False,
                  server_default=ComplaintState.pending.name),
        sa.Column('complainer_id', sa.Integer, nullable=False),
    )


def downgrade():
    # Drop the complaints table
    op.drop_table('complaints')

    # Drop the users table
    op.drop_table('users')
