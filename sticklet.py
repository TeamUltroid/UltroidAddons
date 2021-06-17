# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}sticklet <text>`
   `create random sticker with text.`
"""

import io
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument

from . import *


@ultroid_cmd(pattern="sticklet (.*)")
async def sticklet(event):
    a = await eor(event, "`Processing...`")
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    sticktext = event.pattern_match.group(1)
    if not sticktext:
        return await eor(event, "`Give me some Text`")
    sticktext = textwrap.wrap(sticktext, width=10)
    # converts back the list to a string
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    font_file_ = await ultroid_bot.get_messages(
        entity="@fonthub", filter=InputMessagesFilterDocument, limit=None
    )
    nfont = random.choice(font_file_)
    FONT_FILE = await ultroid_bot.download_media(nfont)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize = 100
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )
    image_stream = io.BytesIO()
    image_stream.name = "leobrownlee.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    await a.delete()
    await ultroid_bot.send_message(
        event.chat_id,
        "{}".format(sticktext),
        file=image_stream,
        reply_to=event.message.reply_to_msg_id,
    )
    os.remove(FONT_FILE)
