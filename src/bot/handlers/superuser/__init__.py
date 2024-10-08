from aiogram import Router

from .add_user import add_user_router
from .scheduler import scheduler_router

superuser_router = Router(name="superuser")
superuser_router.include_router(add_user_router)
superuser_router.include_router(scheduler_router)


__all__ = ["superuser_router"]
