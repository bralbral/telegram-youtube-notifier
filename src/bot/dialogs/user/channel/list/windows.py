from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.kbd import CurrentPage
from aiogram_dialog.widgets.kbd import FirstPage
from aiogram_dialog.widgets.kbd import Group
from aiogram_dialog.widgets.kbd import LastPage
from aiogram_dialog.widgets.kbd import NextPage
from aiogram_dialog.widgets.kbd import PrevPage
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import StubScroll
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.text import Multi
from sulguk import SULGUK_PARSE_MODE

from .constants import ID_STUB_SCROLL
from .getters import scroll_getter
from .on_click import on_delete
from .on_click import on_finish
from .on_click import on_perform_delete
from .on_click import on_perform_update
from .on_click import on_turn_off
from .on_click import on_turn_on
from .widgets import Viewer
from src.bot.states import ChannelsListSG
from src.db.models.user_role import UserRole


def scroll_window():
    return Window(
        Const(
            "⚠️ Channels list is <b>empty</b>.<br/> Add new with <b>/add_channel</b> command.",
            when=F["is_empty"],
        ),
        Multi(
            Viewer("{channels[{current_page}]}"),
            when=~F["is_empty"],
        ),
        Group(
            Row(StubScroll(id=ID_STUB_SCROLL, pages="pages")),
            Row(
                FirstPage(
                    scroll=ID_STUB_SCROLL,
                    text=Format("⏮️ {target_page}"),
                ),
                PrevPage(
                    scroll=ID_STUB_SCROLL,
                    text=Format("◀️"),
                ),
                CurrentPage(
                    scroll=ID_STUB_SCROLL,
                    text=Format("{current_page}"),
                ),
                NextPage(
                    scroll=ID_STUB_SCROLL,
                    text=Format("▶️"),
                ),
                LastPage(
                    scroll=ID_STUB_SCROLL,
                    text=Format("{target_page} ⏭️"),
                ),
            ),
            Group(
                Button(Const("🗑️ Delete"), id="delete", on_click=on_delete),
                Row(
                    Button(Const("✏️ Turn on"), id="off", on_click=on_turn_on),
                    Button(Const("✏️ Turn off"), id="on", on_click=on_turn_off),
                ),
                when=F["role"] == UserRole.SUPERUSER,
            ),
            Row(
                Button(Const("✏️ Turn off"), id="on", on_click=on_turn_off),
                when=F["role"] == UserRole.USER,
            ),
            Button(Const("❌ Exit"), id="finish", on_click=on_finish),
            when=~F["is_empty"],
        ),
        state=ChannelsListSG.scrolling,
        getter=scroll_getter,
        parse_mode=SULGUK_PARSE_MODE,
    )


SWITCH_TO_SCROLLING = SwitchTo(
    text=Const("🔙 No, return me back."), state=ChannelsListSG.scrolling, id="back"
)


def delete_window():
    return Window(
        Const("Are you sure?"),
        Row(
            Button(
                Const("✅ Yes, delete this channel_listing."),
                id="delete",
                on_click=on_perform_delete,
            ),
            SWITCH_TO_SCROLLING,
        ),
        Button(Const("❌ Exit"), id="finish", on_click=on_finish),
        state=ChannelsListSG.delete,
        getter=scroll_getter,
    )


def turn_on_window():
    return Window(
        Const("Are you sure?"),
        Row(
            Button(
                Const("✅ Yes, turn on this channel_listing."),
                id="on",
                on_click=on_perform_update,
            ),
            SWITCH_TO_SCROLLING,
        ),
        Button(Const("❌ Exit"), id="finish", on_click=on_finish),
        state=ChannelsListSG.turn_on,
        getter=scroll_getter,
    )


def turn_off_window():
    return Window(
        Const("Are you sure?"),
        Row(
            Button(
                Const("✅ Yes, turn off this channel_listing."),
                id="off",
                on_click=on_perform_update,
            ),
            SWITCH_TO_SCROLLING,
        ),
        Button(Const("❌ Exit"), id="finish", on_click=on_finish),
        state=ChannelsListSG.turn_off,
        getter=scroll_getter,
    )


__all__ = ["delete_window", "scroll_window", "turn_off_window", "turn_on_window"]
