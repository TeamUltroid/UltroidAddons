# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• {i}smsg <time in seconds> <message>
    SCHEDULES MESSAGE BASED ON SECONDS
"""
import asyncio
from . import *

@ultroid_cmd(pattern="smsg(.*)")
async def snku(ult):
    hm = await eod(ult, ". . .", time=1)
    try:
        sec = ult.text.split(" ")
        time = sec[1]
        msg = sec[2]
    except:
        return await eod(hm, "OOI YOU DID IT WRONG DO .help schedulemsg, time=2")
    await asyncio.sleep(int(time))
    await bot.send_message(ult.chat_id, str(msg))

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})