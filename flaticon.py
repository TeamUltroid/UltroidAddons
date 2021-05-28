# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


"""
✘ Commands Available

• `{i}icon <query>`
    Icon search from flaticon.com and uploading as sticker.

"""

import os
import random
import urllib

import requests
from bs4 import BeautifulSoup as bs

from . import *


@ultroid_cmd(pattern="icon ?(.*)")
async def www(e):
    a = e.pattern_match.group(1)
    if not a:
        return await eor(e, "Give some Text to Get Icon from Flaticon.com")
    tt = await eor(e, "`Processing...`")
    query = a.replace(" ", "%20")
    try:
        link = f"https://www.flaticon.com/search?word={query}"
        ge = requests.get(link).content
        cl = bs(ge, "lxml", from_encoding="utf-8")
        results = cl.find_all(
            "img", src="https://media.flaticon.com/dist/min/img/loader.gif"
        )
        dome = results[random.randrange(0, len(results) - 1)]["data-src"]
        urllib.request.urlretrieve(dome, "sticker.webp")
        await ultroid_bot.send_file(e.chat.id, "sticker.webp")
        os.remove("sticker.webp")
        await tt.delete()
    except Exception:
        await tt.edit("`No Results Found`")
