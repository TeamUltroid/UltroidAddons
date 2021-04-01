# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/UltroidAddons/>

"""
Fetch Random anime quotes from [AnimeChan](https://animechan.vercel.app)

Command : {i}aniquote
"""

import requests

from . import HELP


@ultroid_cmd(pattern="aniquote")
async def _(ult):
    u = await eor(ult, "...")
    try:
        resp = requests.get("https://animechan.vercel.app/api/random").json()
        results = f"**{resp['quote']}**\n"
        results += f" — __{resp['character']} ({resp['anime']})__"
        return await u.edit(results)
    except Exception:
        await u.edit("`Something went wrong LOL ...`")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
