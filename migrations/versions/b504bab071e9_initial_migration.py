"""Initial migration

Revision ID: b504bab071e9
Revises: 
Create Date: 2023-06-25 18:12:04.201177

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b504bab071e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=True),
        sa.Column("firstname", sa.String(length=128), nullable=True),
        sa.Column("lastname", sa.String(length=128), nullable=True),
        sa.Column("password", sa.String(length=128), nullable=True),
        sa.Column("phone", sa.String(length=20), nullable=True),
        sa.Column("iban", sa.String(length=34), nullable=True),
        sa.Column("role", sa.Enum("Approver", "Complainer", "Admin", name="roletype"), nullable=False,
                  server_default="Complainer"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )

    op.create_table(
        "complaints",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=120), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("photo_url", sa.String(length=200), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("create_date", sa.DateTime(), nullable=True, server_default=sa.text("now()")),
        sa.Column("status", sa.Enum("Pending", "Approved", "Rejected", name="complaintstate"), nullable=False,
                  server_default="Pending"),
        sa.Column("complainer_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["complainer_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table("complaints")
    op.drop_table("users")
