"""
✘ Commands Available
• `{i}recognise`
    **How To Use**: Reply To A Image File.
    **Function : **Get information about an image using AWS Recognition.Find out information including detected labels, faces. text and moderation tags.
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import *

@ultroid_cmd(pattern="recognise ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, "reply to media file")
        return
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    ult = await eor(event, "recognising this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=461083923))
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await ult.edit("unblock @Rekognition_Bot and try again")
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            msg = response.message.message
            await ult.edit(msg)
        else:
            await ult.edit("sorry, I couldnt find it")

        await event.client.send_read_acknowledge(conv.chat_id)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})