# " Made by @e3ris for Ultroid "
# < https://github.com/TeamUltroid/Ultroid >
# This Plugin uses @Text2gifBot.

"""
✘ **Makes Fancy Gif from your Words!**

✘ ** text2gif -> t2g **
 eg : `{i}t2g <some_text>`
"""

import emoji
import re

from telethon import functions, types
from random import randint as rnd

from . import *


chat = "text2gifBot"
def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)


@ultroid_cmd(pattern="t2g ?(.*)")
async def t2g(e):
    if e.fwd_from:
        return
    eris = await eor(e, "`...`")
    reply_to = e.reply_to_msg_id if e.is_reply else None
    input_args = e.pattern_match.group(1) 
    if not input_args:
        input_args = "No Text was Given :(("
    args = remove_emoji(input_args)
    try:
        t2g = await ultroid.inline_query(chat, args)
        to_me = await t2g[rnd(0, 27)].click("me")
        done = await ultroid.send_file(
            e.chat_id,
            to_me,
            reply_to=reply_to,
        )
        await eris.delete()
        await to_me.delete()
    except Exception as fn:
        return await eod(eris, f"`{fn}`")
    await cleargif(done)



async def cleargif(gif_):
    try:
        await ultroid(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=gif_.media.document.id,
                    access_hash=gif_.media.document.access_hash,
                    file_reference=gif_.media.document.file_reference,
                ), 
                unsave=True,
            )
        )
    except Exception:
        pass


HELP.update({f"{_name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})

