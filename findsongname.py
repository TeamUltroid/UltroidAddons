#Made By senku And **Inspired From Cat**

"""
✘ Commands Available
• `{i}findsong`
        gives you the name of the song

"""

import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import HELP


@ultroid_cmd(pattern="findsong$")
async def _(ult):
    if ult.fwd_from:
        return
    if not ult.reply_to_msg_id:
        await edit_delete(ult, "Reply to an audio message.")
        return
    reply_message = await ult.get_reply_message()
    chat = "@auddbot"
    oofsnku = await edit_or_reply(ult, "Identifying the song")
    async with ult.client.conversation(chat) as conv:
        try:
            start_msg = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await oofsnku.edit("An error while identifying the song. Try to use a 5-10s long audio message.")
            await oofsnku.edit("Wait just a sec...")
            result = await conv.get_response()
            await ult.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await oofsnku.edit("Please unblock (@auddbot) and try again")
            return
    namem = f"**Song Name : **`{result.text.splitlines()[0]}`\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await oofsnku.edit(namem)
    
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
