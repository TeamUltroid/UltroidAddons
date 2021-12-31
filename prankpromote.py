# Written By @senku_ishigamiii and inspiried from DarkCobra Wala Plugin

"""
✘ Commands Available

• `{i}pprank`
    Show Fake Promotion
"""

import asyncio

from . import *


@ultroid_cmd(pattern="pprank")
async def pprank(ult):
    msg = await ult.eor("**PROMOTING USER..**")
    await asyncio.sleep(1)
    await msg.edit("**PROMOTING USER...**")
    await asyncio.sleep(1)
    await msg.edit("**GIVING RIGHTS**")
    await asyncio.sleep(1)
    await msg.edit("**PROMOTED USER SUCCESSFULLY**")
