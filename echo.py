# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_echo")

from telethon.utils import get_display_name

from . import events, udB, ultroid_bot, ultroid_cmd, LOGS, types

# Functions moved from echo_db.py
def get_stuff():
    return udB.get_key("ECHO") or {}


def add_echo(chat, user):
    x = get_stuff()
    if k := x.get(int(chat)):
        if user not in k:
            k.append(int(user))
        x.update({int(chat): k})
    else:
        x.update({int(chat): [int(user)]})
    return udB.set_key("ECHO", x)


def rem_echo(chat, user):
    x = get_stuff()
    if k := x.get(int(chat)):
        if user in k:
            k.remove(int(user))
        x.update({int(chat): k})
    return udB.set_key("ECHO", x)


def check_echo(chat, user):
    x = get_stuff()
    if (k := x.get(int(chat))) and int(user) in k:
        return True


def list_echo(chat):
    x = get_stuff()
    return x.get(int(chat))


@ultroid_cmd(pattern="addecho( (.*)|$)")
async def echo(e):
    r = await e.get_reply_message()
    if r:
        user = r.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Reply To A user.", time=5)
    if check_echo(e.chat_id, user):
        return await e.eor("Echo already activated for this user.", time=5)
    add_echo(e.chat_id, user)
    ok = await e.client.get_entity(user)
    user = f"{ok.first_name} {ok.last_name}" if ok.last_name else ok.first_name
    await e.eor(f"Activated Echo For {user}.")


@ultroid_cmd(pattern="remecho( (.*)|$)")
async def rm(e):
    r = await e.get_reply_message()
    if r:
        user = r.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("Reply To A User.", time=5)
    if check_echo(e.chat_id, user):
        rem_echo(e.chat_id, user)
        ok = await e.client.get_entity(user)
        user = f"{ok.first_name} {ok.last_name}" if ok.last_name else ok.first_name
        return await e.eor(f"Deactivated Echo For {user}.")
    await e.eor("Echo not activated for this user")


@ultroid_cmd(pattern="listecho$")
async def lstecho(e):
    k = list_echo(e.chat_id)
    if k:
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            try:
                ok = await e.client.get_entity(x)
                kk = f"{ok.first_name} {ok.last_name}" if ok.last_name else ok.first_name
                user += f"•{kk}\n"
            except BaseException:
                user += f"•[{x}](tg://user?id={x})\n"
        await e.eor(user)
    else:
        await e.eor("`No echo activated here!`", time=5)


@ultroid_bot.on(events.NewMessage(incoming=True))
async def samereply(e):
    if check_echo(e.chat_id, e.sender_id):
        if e.text:
            text = e.text
            if e.reply_to:
                if e.reply_to.reply_to_top_id:
                    reply_msg = await e.get_reply_message()
                    if reply_msg.text:
                        text = reply_msg.text
            try:
                await e.client.send_message(e.chat_id, text, reply_to=e.id)
            except Exception as er:
                print(er)
        if e.media:
            await e.client.send_file(e.chat_id, e.media, reply_to=e.id)


# Add a separate handler for echo replies
async def echo_handler(e):
    sender = await e.get_sender()
    if not isinstance(sender, types.User) or sender.bot:
        return
    if check_echo(e.chat_id, e.sender_id):
        try:
            await e.respond(e.message)
        except Exception as er:
            LOGS.exception(er)

# Register the handler
ultroid_bot.add_handler(echo_handler, events.NewMessage(incoming=True))
