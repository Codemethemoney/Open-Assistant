"""Adds text labels table.

Revision ID: 067c4002f2d9
Revises: 0daec5f8135f
Create Date: 2022-12-25 17:05:21.208843

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "067c4002f2d9"
down_revision = "0daec5f8135f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "text_labels",
        sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("created_date", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.Column("post_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("labels", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("api_client_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("text", sqlmodel.sql.sqltypes.AutoString(length=65536), nullable=False),
        sa.ForeignKeyConstraint(
            ["api_client_id"],
            ["api_client.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["post.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("text_labels")
    # ### end Alembic commands ###