from aiogram.types import BotCommand


def superuser_commands() -> list[BotCommand]:
    commands = [
        BotCommand(command="add_user", description="Add user to bot."),
        BotCommand(command="scheduler_start", description="Start scheduler."),
        BotCommand(command="scheduler_pause", description="Stop scheduler."),
    ]
    return commands


def user_commands() -> list[BotCommand]:
    commands = [
        BotCommand(command="cancel", description="Clear current state."),
        BotCommand(command="add_channel", description="Add channel_listing."),
        BotCommand(
            command="channels", description="Start Channels Administration Dialog."
        ),
    ]
    return commands


__all__ = ["superuser_commands", "user_commands"]
