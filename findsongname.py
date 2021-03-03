#Made By senku And **Inspired From Cat**
# Ported for Ultroid Userbot


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
    if not ult.is_reply:
        return await eor(ult, 'Reply to an audio message.')
    reply_message = await ult.get_reply_message()
    chat = "@auddbot"
    oofsnku = await eor(ult, '`Identifying the song...`')
    async with ult.client.conversation(chat) as conv:
        try:
            start_msg = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith('Audio received'):
                return await oofsnku.edit('An error while identifying the song. Try to use a 5-10s long audio message.')
            await oofsnku.edit("`Wait just a sec...`")
            result = await conv.get_response()
            await ult.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await oofsnku.edit('Please unblock (@auddbot) and try again')
    namem = f"**Song Name : **`{result.text.splitlines()[0]}`\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await oofsnku.edit(namem)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
