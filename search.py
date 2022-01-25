# Ported From https://github.com/kaif-00z/ForwarderBot
# (c) @kaif-00z for @TeamUltroid

"""
`/search <channel/group id> <query>` Will send all the related file/message/media from id
"""


from . import *
import re

X = []
Z = []

@asst_cmd(pattern="/search")
async def src(event):
    chat = event.text.split()[1]
    query = event.text.split(" ", maxsplit=1)[1]
    btn = [Button.inline("CANCEL PROCESS", data="cnc")]
    x = await event.reply("`searching...`", buttons=btn)
    async for message in ultroid_bot.iter_messages(chat, search=query):
        if message:
            if event.sender_id not in X:
                X.append(event.sender_id)
            msg = await asst_cmd.get_messages(chat, ids=message.id)
            await asst_cmd.send_message(event.chat_id, msg)
            if event.sender_id in Z:
                Z.remove(event.sender_id)
                return await x.delete()
            await asyncio.sleep(1)
            continue
    if event.sender_id not in X:
        await asst_cmd.send_message(
            event.chat_id,
            f"**Nothing Found Related To Keyword :** `{query}`",
        )
    else:
        await asst_cmd.send_message(
            event.chat_id,
            f"All Files Related To Keyword : `{query}` sent successfully.",
        )
        X.remove(event.sender_id)
    await x.delete()

@callback(re.compile("cnc"))
async def _(e):
    Z.append(e.sender_id)
