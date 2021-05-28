# from Freaky Userbot
# Ported for Ultroid Userbot

"""
✘ Commands Available -

• `{i}shorturl <url>`
   Get the shorted form of given url.

"""

import pyshorteners

from . import *


@ultroid_cmd(pattern="shorturl ?(.*)")
async def vom(event):
    a = await eor(event, "`Processing...`")
    try:
        link = event.pattern_match.group(1)
        if not link:
            return await a.edit("`Please Give me a Link to Shorten`")
        txt = pyshorteners.Shortener()
        if "http://tinyurl.com" in link.lower():
            ok = txt.tinyurl.expand(link)
            eu = "Expanded"
        else:
            ok = txt.tinyurl.short(link)
            eu = "Shortned"
        short = (
            f"**Url {eu}**\n**Given Link** ➠ {link}\n"
            f"**{eu} Link** ➠ [{eu} Link]({ok})"
        )
        await a.edit(short)
    except Exception as e:
        await a.edit("SomeThing Went Wrong. \n**ERROR** : " + str(e))
