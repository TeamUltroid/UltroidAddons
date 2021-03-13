#Written By @senku_ishigamiii and inspiried from DarkCobra Wala Plugin

"""
✘ Commands Available
• `{i}pprank`
    Show Fake Promotion
"""

import asyncio
from . import *

@ultroid_cmd(pattern="pprank")
async def pprank(ult):
    if not ult.text[0].isalpha() and ult.text[0] not in ("/", "#", "@", "!"):
        await ult.edit("**PROMOTING USER..***")
        await asyncio.sleep(1)
        await ult.edit("**PROMOTING USER...**")
        await asyncio.sleep(1)
        await ult.edit("**GIVING RIGHTS**")
        await asyncio.sleep(1)
        await ult.edit("**PROMOTED USER SUCCESSFULLY**")
        
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
