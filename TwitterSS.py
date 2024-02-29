# Credits @HamimCM
# Ported from Ultroid Crypto Add-on
# Ported for Ultroid < https://github.com/TeamUltroid/Ultroid >

"""
✘ Commands Available
• `{i}tss <Twitter link or ID>`

E.g: https://twitter.com/jack/status/969234275420655616
Or ID:
E.g: 969234275420655616

    Gives Screenshot of Tweet.
    """

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from . import *

@ultroid_cmd(pattern="tss(.*)$")
async def demn(ult):
    input = ult.pattern_match.group(1)
    chat = "@TweetShotBot"
    await ult.edit("Please Wait")
    async with ult.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1073646153))
            await ult.client.send_message(chat, f"{input}")
            response = await response
        except YouBlockedUserError:
            await ult.reply("Boss! Please Unblock @TweetShotBot")    
            return
        x = response.text
        z = x.split("\n")[(len(x.split("\n")))-1]
        await ult.reply(input, file=response.media)

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})