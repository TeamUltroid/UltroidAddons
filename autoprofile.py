#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# .tweet made for ultroid

# .uta ported from Dark-Cobra

"""
✘ Commands Available -

• `{i}autoname` - Starts AUTONAME.
• `{i}stopname` - Stops AUTONAME.

"""

from . import *
from telethon.tl.functions.account import UpdateProfileRequest


@ultroid_cmd(pattern="(auto|stop)name$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
      udB.delete("AUTONAME")
      await eor(event, "`AUTONAME has been Stopped !`")
      return
    udB.set("AUTONAME", "True")
    while True:
        getn = udB.get("AUTONAME")
        if not getn:
            return
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{OWNER_NAME}⚡ {DM} 🗓️"
        await ultroid_bot(
                UpdateProfileRequest( 
                    first_name=name
                )
            )
        await asyncio.sleep(1000)
    await eor(event, "`AutoName has Been Started`")

