from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State
from aiogram.types import Message

from ...filters import RoleFilter
from ...filters import UserRole

acl_router = Router(name="acl")


@acl_router.message(
    Command("promote"),
    RoleFilter(role=[UserRole.SUPERUSER]),
    State(state="*"),
)
async def promote_user_to_admin(message: Message, **kwargs):
    await message.answer("Added.")


@acl_router.message(
    Command("revoke"),
    RoleFilter(role=[UserRole.SUPERUSER]),
    State(state="*"),
)
async def revoke_user(message: Message, **kwargs):
    await message.answer("Deleted.")


__all__ = ["acl_router"]