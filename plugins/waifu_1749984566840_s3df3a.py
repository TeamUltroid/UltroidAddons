# Ported Plugin

"""
✘ Commands Available -

• `{i}waifu <text>`
    paste text on random stickers.
"""

import re

from . import *


@ultroid_cmd(
    pattern="waifu ?(.*)",
)
async def waifu(animu):
    xx = await eor(animu, get_string("com_1"))
    # """Creates random anime sticker!"""
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await xx.edit(get_string("sts_1"))
            return
    waifus = [32, 33, 37, 40, 41, 42, 58, 20]
    finalcall = "#" + (str(random.choice(waifus)))
    sticcers = await animu.client.inline_query(
        "stickerizerbot",
        f"{finalcall}{(deEmojify(text))}",
    )
    await sticcers[0].click(
        animu.chat_id,
        reply_to=animu.reply_to_msg_id,
        silent=bool(animu.is_reply),
        hide_via=True,
    )
    await xx.delete()
