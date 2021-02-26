#Written By @senku_ishigamiii and inspiried from DarkCobra Wala Plugin
import asyncio

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