# credits @telebot and @maxprogrammer007 for editing
# ported from <https://github.com/xditya/TeleBot/blob/master/telebot/plugins/quotly.py>
# Ported for Ultroid < https://github.com/TeamUltroid/Ultroid >   


"""Available commands: 

   .quotly - sticker conversion by @QuotlyBot
   
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@ultroid_cmd(pattern="quotly")
async def _(event):
    if not event.reply_to_msg_id:
        return await eor(event, "```Reply to any user message.```")
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        return await eor(event, "```Reply to text message```")
    chat = "@QuotLyBot"
    reply_message.sender
    ac = await eor(event, "```Making a Quote```")
    async with ultroid_bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await ultroid_bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.reply("```Please unblock @QuotLyBot and try again```")
        if response.text.startswith("Hi!"):
            await eor(
                event,
                "```Can you kindly disable your forward privacy settings for good?```",
            )
        else:
            await ac.delete()
            await ultroid_bot.send_message(event.chat_id, response.message)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
