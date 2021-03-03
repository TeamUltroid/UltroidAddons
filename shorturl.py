# from Freaky Userbot
# Add pyshorteners in requirements.txt

import pyshorteners

from . import HELP

@ultroid_cmd(pattern="shorturl ?(.*)")
async def vom(event):
    a = await eor(event,"`Processing...`")
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
            f"<b>Url {eu}</b> \n<b><u>Given Link</u></b> ➠ <code>{link}</code> \n"
            f"<b><u>{eu} Link</u></b> ➠ <a href='{ok}'>Short Link</a>"
        )
        await a.edit(short, parse_mode="HTML")
    except Exception as e:
        await a.edit("SomeThing Went Wrong. \nError : " + e)


HELP.update(
    {
        "shorturl": f"UrlShortner\
\n\nSyntax : {Var.HNDLR}shorturl <link>\
\nUsage : Shortens Your Url\
if used shorten link, it will be expanded"
    }
)
