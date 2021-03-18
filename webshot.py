# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}webshot <Link>`
    Take Screenshots of Website.

"""

from . import *
import requests as r
import urllib

@ultroid_cmd(pattern="webshot ?(.*)")
async def webshot(ult):
    cl = ult.pattern_match.group(1)
    if not cl:
        return await eor(ult, "Give a Url Please to Perform this Task !")
    msg = await eor(ult, "`Performing a Web-Shot...\nKeep Patience !`")
    SHOTAPI = udB.get("WEBSHOTAPI")
    PR = urllib.parse.quote(cl)
    LINK = f"https://screenshotapi.net/api/v1/screenshot?url={PR}&token="
    if SHOTAPI:
        LINK += SHOTAPI
    mk = r.get(LINK).json()
    photo = mk["screenshot"]
    await ultroid_bot.send_file(ult.chat_id,
                                photo)
    await msg.delete()
  

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
