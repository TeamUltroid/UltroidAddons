# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_blacklist")

from telethon.tl.types import Channel

from . import events, get_string, udB, ultroid_bot, ultroid_cmd

# Functions moved from blacklist_db.py
def get_stuff():
    return udB.get_key("BLACKLIST_DB") or {}


def add_blacklist(chat, word):
    ok = get_stuff()
    if ok.get(chat):
        for z in word.split():
            if z not in ok[chat]:
                ok[chat].append(z)
    else:
        ok.update({chat: [word]})
    return udB.set_key("BLACKLIST_DB", ok)


def rem_blacklist(chat, word):
    ok = get_stuff()
    if ok.get(chat) and word in ok[chat]:
        ok[chat].remove(word)
        return udB.set_key("BLACKLIST_DB", ok)


def list_blacklist(chat):
    ok = get_stuff()
    if ok.get(chat):
        txt = "".join(f"👉`{z}`\n" for z in ok[chat])
        if txt:
            return txt


def get_blacklist(chat):
    ok = get_stuff()
    if ok.get(chat):
        return ok[chat]


@ultroid_cmd(pattern="blacklist( (.*)|$)", admins_only=True)
async def af(e):
    wrd = e.pattern_match.group(1).strip()
    chat = e.chat_id
    if not (wrd):
        return await e.eor(get_string("blk_1"))
    wrd = e.text.split(maxsplit=1)[1]
    add_blacklist(chat, wrd)
    await e.eor(get_string("blk_2").format(wrd))


@ultroid_cmd(pattern="remblacklist( (.*)|$)", admins_only=True)
async def rf(e):
    wrd = e.pattern_match.group(1).strip()
    chat = e.chat_id
    if not wrd:
        return await e.eor(get_string("blk_3"))
    wrd = e.text.split(maxsplit=1)[1]
    if rem_blacklist(chat, wrd):
        await e.eor(get_string("blk_4").format(wrd))
    else:
        await e.eor(get_string("blk_5"))


@ultroid_cmd(pattern="listblacklist$", admins_only=True)
async def lsnote(e):
    if x := list_blacklist(e.chat_id):
        await e.eor(get_string("blk_6").format(x))
    else:
        await e.eor(get_string("blk_7"))


async def blacklist(e):
    if not get_blacklist(e.chat_id):
        return
    xx = get_blacklist(e.chat_id)
    if getattr(e, "sender", None) and isinstance(e.sender, Channel):
        return
    if not (
        isinstance(e.text, str)
        and ("chat.whatsapp.com" in e.text.lower())
        and e.sender
        and hasattr(e.sender, "username")
        and e.sender.username == "Channel_Bot"
    ):
        text = e.text.lower().split()
        for x in xx:
            if x.lower() in text:
                try:
                    await e.delete()
                except Exception:
                    pass
                break


if get_stuff():
    ultroid_bot.add_handler(blacklist, events.NewMessage(incoming=True))
