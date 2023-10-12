"""init

Revision ID: 0fa064c1269d
Revises: 
Create Date: 2023-10-10 22:12:40.058823

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0fa064c1269d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=True),
        sa.Column("firstname", sa.String(length=255), nullable=True),
        sa.Column("lastname", sa.String(length=255), nullable=True),
        sa.Column("is_admin", sa.Boolean(), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", name="ix_uniq_telegram_user_id"),
    )
    op.create_index(op.f("ix_users_firstname"), "users", ["firstname"], unique=False)
    op.create_index(op.f("ix_users_is_admin"), "users", ["is_admin"], unique=False)
    op.create_index(
        op.f("ix_users_is_superuser"), "users", ["is_superuser"], unique=False
    )
    op.create_index(op.f("ix_users_lastname"), "users", ["lastname"], unique=False)
    op.create_index(op.f("ix_users_user_id"), "users", ["user_id"], unique=False)
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=False)
    op.create_table(
        "channels",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("url", sa.String(length=255), nullable=False),
        sa.Column("label", sa.String(length=255), nullable=False),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url", name="ix_uniq_url"),
    )
    op.create_index(op.f("ix_channels_enabled"), "channels", ["enabled"], unique=False)
    op.create_index(op.f("ix_channels_label"), "channels", ["label"], unique=False)
    op.create_index(op.f("ix_channels_url"), "channels", ["url"], unique=False)
    op.create_table(
        "channel_errors",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("count", sa.BigInteger(), nullable=True),
        sa.Column("channel_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["channel_id"], ["channels.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("channel_id", name="ix_uniq_channel_id"),
    )
    op.create_index(
        op.f("ix_channel_errors_count"), "channel_errors", ["count"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_channel_errors_count"), table_name="channel_errors")
    op.drop_table("channel_errors")
    op.drop_index(op.f("ix_channels_url"), table_name="channels")
    op.drop_index(op.f("ix_channels_label"), table_name="channels")
    op.drop_index(op.f("ix_channels_enabled"), table_name="channels")
    op.drop_table("channels")
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_index(op.f("ix_users_user_id"), table_name="users")
    op.drop_index(op.f("ix_users_lastname"), table_name="users")
    op.drop_index(op.f("ix_users_is_superuser"), table_name="users")
    op.drop_index(op.f("ix_users_is_admin"), table_name="users")
    op.drop_index(op.f("ix_users_firstname"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###