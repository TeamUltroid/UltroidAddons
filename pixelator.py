# 2020 @FUSUF #
# @ASENAUSERBOT #
# https://t.me/asenaplugin/228

# Ported for Ultroid


from . import *
from telethon.errors.rpcerrorlist import YouBlockedUserError


@ultroid_cmd(pattern="pixelator")
async def pixelator(event):
    reply_message = await event.get_reply_message() 
    if not (reply_message and reply_message.media):
        await eor(event, "`Reply to a photo`")
        return
    chat = "@pixelatorbot"
    msg = await eor(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:     
            await event.client.send_message(chat, reply_message)
        except YouBlockedUserError:
            await msg.edit(f"`Unblock` {chat} `and try again...`")
            return
        response = await conv.wait_event(events.NewMessage(incoming=True, from_users="@PixelatorBot"))
        await event.client.send_read_acknowledge("@PixelAtorBot")
        if response.text.startswith("Looks"):
            await msg.edit("`I cant pixel this..!`")
        else:
            await msg.respond("`Pixelated !`", file=response.media)
            await msg.delete()
