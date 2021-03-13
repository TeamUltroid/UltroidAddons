#inspired from bin.py which was made by @danish_00 
#written by @senku_ishigamiii/@Uzumaki_Naruto_XD

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest


@ultroid_cmd(pattern="limited$")
async def demn(ult):
    chat = "@SpamBot"
    await ult.edit("Checking If You Are Limited...")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=178220800))
            await ult.client.send_message(chat, "/start")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @SpamBot ")
            return
        await eor(ult, response.message.message)