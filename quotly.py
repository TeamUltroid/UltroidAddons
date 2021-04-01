#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


"""
✘ Commands Available -

• `{i}quotly | {i}qbot <colour name/code><replying a message>`
    send stickers to current chat with @QuotlyBot.

"""

import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *

ERR = "`Can you kindly disable your forward privacy settings for good?`"


@ultroid_cmd(pattern="(quotly|qbot) ?(.*)")
async def _(event):
    if not event.reply_to_msg_id:
        return await eor(event, "```Reply to any user message.```")
    reply_message = await event.get_reply_message()
    chat = "@QuotLyBot"
    reply_message.sender
    ac = await eor(event, "```Making a Quote```")
    col = event.pattern_match.group(2)
    async with ultroid_bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            er = await ultroid_bot.forward_messages(chat, reply_message)
            if not len(col) == 0:  # Bad way
                await asyncio.sleep(3)
                await er.reply(f"/q {col}")
            response = await response
            await ultroid_bot.send_read_acknowledge(chat)
        except YouBlockedUserError:
            return await event.reply("```Please unblock @QuotLyBot and try again```")
        if response.text.startswith("Hi!"):
            await eor(event, ERR)
        else:
            await ac.delete()
            await ultroid_bot.send_message(event.chat_id, response.message)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
