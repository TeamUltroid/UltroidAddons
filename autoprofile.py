#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# Ported Plugin

"""
✘ Commands Available -

• `{i}autoname`
   `Starts AUTONAME`.

• `{i}stopname`
   `Stops AUTONAME.`

• `{i}autobio`
   `Starts AUTOBIO.`

• `{i}stopbio`
   `Stops AUTOBIO.`
"""

from . import *
import random
from telethon.tl.functions.account import UpdateProfileRequest


@ultroid_cmd(pattern="(auto|stop)name$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
      udB.delete("AUTONAME")
      await eor(event, "`AUTONAME has been Stopped !`")
      return
    udB.set("AUTONAME", "True")
    await eod(event, "`Started AUTONAME`")
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


@ultroid_cmd(pattern="(auto|stop)bio$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
      udB.delete("AUTOBIO")
      await eor(event, "`AUTOBIO has been Stopped !`")
      return
    udB.set("AUTOBIO", "True")
    await eod(event, "`Started AUTONAME`")
    BIOS = ["Busy Today !",
            "ULTROID USER",
            "Enjoying Life!",
            "Unique as Always!"
            "Sprinkling a bit of magic",
            "Intelligent !"]
    while True:
        getn = udB.get("AUTOBIO")
        if not getn:
            return
        BIOMSG = random.choice(BIOS)
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"📅{DM} | {BIOMSG} | ⌚️{HM}"
        await ultroid_bot(
                UpdateProfileRequest( 
                    about=name,
                )
            )
        await asyncio.sleep(1000)
