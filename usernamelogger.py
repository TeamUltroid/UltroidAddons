# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}enableulog`
    Enable username logging in the bot.

• `{i}disableulog`
    Disable username logging in the bot.
"""

from telethon import events, types

from . import LOG_CHANNEL, asst, get_string, udB, ultroid_bot, ultroid_cmd

@ultroid_cmd(pattern="enableulog$")
async def enablelog(e):
    if udB.get_key("USERNAME_LOG"):
        return await e.eor("`Username logging is already enabled!`")
    udB.set_key("USERNAME_LOG", True)
    await e.eor("`Username logging enabled successfully!`")

@ultroid_cmd(pattern="disableulog$")
async def disablelog(e):
    if not udB.get_key("USERNAME_LOG"):
        return await e.eor("`Username logging is already disabled!`")
    udB.del_key("USERNAME_LOG")
    await e.eor("`Username logging disabled successfully!`")

async def uname_stuff(id, uname, name):
    if udB.get_key("USERNAME_LOG"):
        old_ = udB.get_key("USERNAME_DB") or {}
        old = old_.get(id)
        # Ignore Name Logs
        if old and old == uname:
            return
        if old and uname:
            await asst.send_message(
                LOG_CHANNEL,
                get_string("can_2").format(old, uname),
            )
        elif old:
            await asst.send_message(
                LOG_CHANNEL,
                get_string("can_3").format(f"[{name}](tg://user?id={id})", old),
            )
        elif uname:
            await asst.send_message(
                LOG_CHANNEL,
                get_string("can_4").format(f"[{name}](tg://user?id={id})", uname),
            )

        old_[id] = uname
        udB.set_key("USERNAME_DB", old_)

# Username collection from messages
async def username_from_msg(e):
    sender = await e.get_sender()
    chat = await e.get_chat()
    if not isinstance(sender, types.User) or sender.bot:
        return
    if e.is_group and sender.username:
        await uname_stuff(e.sender_id, sender.username, sender.first_name)
    elif e.is_private and chat.username:
        await uname_stuff(e.sender_id, chat.username, chat.first_name)

# Username change handler
@ultroid_bot.on(events.Raw(types.UpdateUserName))
async def uname_change(e):
    await uname_stuff(e.user_id, e.usernames[0] if e.usernames else None, e.first_name)

# Register message handler if logging is enabled
if udB.get_key("USERNAME_LOG"):
    ultroid_bot.add_handler(username_from_msg, events.NewMessage(incoming=True)) 