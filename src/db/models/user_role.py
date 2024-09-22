import enum

from sqlalchemy import Column
from sqlalchemy import Enum
from sqlmodel import Field

from .base import BaseSQLModel


class UserRole(enum.IntEnum):
    USER = 0
    ADMIN = 1


class UserRoleModel(BaseSQLModel):

    __tablename__ = "user_roles"

    role: UserRole = Field(
        sa_column=Column(
            Enum(UserRole), default=UserRole.USER, nullable=False, index=False
        )
    )


__all__ = ["UserRoleModel"]