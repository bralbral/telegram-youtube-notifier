from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Sequence

from .base import BaseDAO
from src.db.models import ChannelTypeModel


class ChannelTypeDAO(BaseDAO[ChannelTypeModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, ChannelTypeModel)

    async def get_first(self, *args, **kwargs) -> Optional[ChannelTypeModel]:
        return await super().get_first(*args, **kwargs)

    async def get_many(self, *args, **kwargs) -> Sequence[ChannelTypeModel]:
        return await super().get_many(*args, **kwargs)

    async def create(self, obj: ChannelTypeModel) -> Optional[ChannelTypeModel]:
        return await super().create(obj)

    async def get_or_create(self, **kwargs) -> tuple[ChannelTypeModel, bool]:
        return await super().get_or_create(**kwargs)

    async def update(self, obj: ChannelTypeModel) -> Optional[ChannelTypeModel]:
        return await super().update(obj)

    async def delete(self, id: int) -> bool:
        return await super().delete(id)


__all__ = ["ChannelTypeDAO"]
