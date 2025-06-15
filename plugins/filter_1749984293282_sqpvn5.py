# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_filter")

import os
import re

from telethon.tl.types import User
from telethon.utils import get_display_name

from pyUltroid.fns.tools import create_tl_btn, format_btn, get_msg_button

from . import events, get_string, mediainfo, udB, ultroid_bot, ultroid_cmd, upload_file
from ._inline import something

# Functions moved from filter_db.py
def get_stuff():
    return udB.get_key("FILTERS") or {}


def add_filter(chat, word, msg, media, button):
    ok = get_stuff()
    if ok.get(chat):
        ok[chat].update({word: {"msg": msg, "media": media, "button": button}})
    else:
        ok.update({chat: {word: {"msg": msg, "media": media, "button": button}}})
    udB.set_key("FILTERS", ok)


def rem_filter(chat, word):
    ok = get_stuff()
    if ok.get(chat) and ok[chat].get(word):
        ok[chat].pop(word)
        udB.set_key("FILTERS", ok)


def rem_all_filter(chat):
    ok = get_stuff()
    if ok.get(chat):
        ok.pop(chat)
        udB.set_key("FILTERS", ok)


def get_filter(chat):
    ok = get_stuff()
    if ok.get(chat):
        return ok[chat]


def list_filter(chat):
    ok = get_stuff()
    if ok.get(chat):
        return "".join(f"👉 `{z}`\n" for z in ok[chat])


@ultroid_cmd(pattern="addfilter( (.*)|$)")
async def af(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    wt = await e.get_reply_message()
    chat = e.chat_id
    if not (wt and wrd):
        return await e.eor(get_string("flr_1"))
    btn = format_btn(wt.buttons) if wt.buttons else None
    if wt and wt.media:
        wut = mediainfo(wt.media)
        if wut.startswith(("pic", "gif")):
            dl = await wt.download_media()
            variable = upload_file(dl)
            os.remove(dl)
        elif wut == "video":
            if wt.media.document.size > 8 * 1000 * 1000:
                return await e.eor(get_string("com_4"))
            dl = await wt.download_media()
            variable = upload_file(dl)
            os.remove(dl)
        else:
            variable = None
    else:
        variable = None
    if not wt.text and not variable:
        return await e.eor(get_string("flr_2"))
    txt = wt.text or None
    if txt:
        if button := get_msg_button(txt):
            txt = button[0]
            button = button[1]
        elif btn:
            button = btn
        else:
            button = None
    add_filter(chat, wrd, txt, variable, button)
    await e.eor(get_string("flr_3").format(wrd))
    ultroid_bot.add_handler(filter_func, events.NewMessage())


@ultroid_cmd(pattern="remfilter( (.*)|$)")
async def rf(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    chat = e.chat_id
    if not wrd:
        return await e.eor(get_string("flr_4"))
    rem_filter(chat, wrd)
    await e.eor(get_string("flr_5").format(wrd))


@ultroid_cmd(pattern="listfilter$")
async def lsnote(e):
    if x := list_filter(e.chat_id):
        await e.eor(get_string("flr_6").format(x))
    else:
        await e.eor(get_string("flr_7"))


async def filter_func(e):
    if isinstance(e.sender, User) and e.sender.bot:
        return
    xx = (e.text).lower()
    chat = e.chat_id
    if x := get_filter(chat):
        for c in x:
            pat = r"( |^|[^\w])" + re.escape(c) + r"( |$|[^\w])"
            if re.search(pat, xx):
                if k := x.get(c):
                    msg = k["msg"]
                    media = k["media"]
                    if k.get("button"):
                        btn = create_tl_btn(k["button"])
                        return await something(e, msg, media, btn)
                    await e.reply(msg, file=media)


if get_stuff():
    ultroid_bot.add_handler(filter_func, events.NewMessage())
