# from Freaky Userbot
# Add pyshorteners in requirements.txt

import pyshorteners

from . import HELP

@ultroid_cmd(pattern="shorturl ?(.*)")
async def vom(event):
    a = await eor(event,"`Processing...`")
    try:
        link = event.pattern_match.group(1)
        txt = pyshorteners.Shortener()
        ok = txt.tinyurl.short(link)
        short = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ <code>{link}</code> \n"
            f"<b><u>Shortened Link</u></b> ➠ <a href='{ok}'>Short Link</a>"
        )
        await a.edit(short, parse_mode="HTML")
    except Exception as e:
        await a.edit("SomeThing Went Wrong. \nError : " + e)


HELP.update(
    {
        "shorturl": f"UrlShortner\
\n\nSyntax : {Var.HNDLR}shorturl <link>\
\nUsage : Shortens Your Url"
    }
)
