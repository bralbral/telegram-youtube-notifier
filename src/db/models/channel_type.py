import enum

from sqlalchemy import Column
from sqlalchemy import Enum
from sqlmodel import Field

from .base import BaseSQLModel


class ChannelType(enum.IntEnum):
    YOUTUBE = 0
    TWITCH = 1


class ChannelTypeModel(BaseSQLModel):

    __tablename__ = "channel_types"

    type: ChannelType = Field(
        sa_column=Column(
            Enum(ChannelType), default=ChannelType.YOUTUBE, nullable=False, index=False
        )
    )


__all__ = ["ChannelTypeModel"]