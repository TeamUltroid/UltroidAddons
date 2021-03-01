# from Freaky Userbot
# Add pyshorteners in requirements.txt

import pyshorteners

from . import *

@ultroid_cmd(pattern="shorturl ?(.*)")
async def vom(event):
    try:
        link = event.pattern_match.group(1)
        txt = pyshorteners.Shortener()
        ok = txt.tinyurl.short(link)
        short = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ <code>{link}</code> \n"
            f"<b><u>Shortened Link</u></b> ➠ <a href='{ok}'>Short Link</a>"
        )
        await event.edit(short, parse_mode="HTML")
    except Exception as e:
        await event.edit("SomeThing Went Wrong. \nError : " + e)


HELP.update(
    {
        "urlshortner": "UrlShortner\
\n\nSyntax : .shorturl <link>\
\nUsage : Shortens Your Url"
    }
)
