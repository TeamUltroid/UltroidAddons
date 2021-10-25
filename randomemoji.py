"""
GET random emoji in Image Format.
Usage - .randomemoji.
"""

# By - SantaYamin aka Nikola.N

import os

from multiutility import EmojiCreator
from . import *

Emoji = EmojiCreator())


@ultroid_cmd(
    "randomemoji"
)
async def app(e):
    msg_ = await eor(e, "Generating RaNDOmEMoJi for YoU...")
    emoji = Emoji.get_random()
    await msg_.reply("**---- Random Emoji ----**", file=emoji)
    os.remove(emoji)
    await msg_.delete()
