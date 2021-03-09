"""
Fetch Random anime quotes from [AnimeChan](https://animechan.vercel.app)

Command : {i}aniquote
"""
from . import HELP
import requests

@ultroid_cmd(pattern="aniquote")
async def _(u):
  await u.edit("...")
  try:
    resp = requests.get("https://animechan.vercel.app/api/random").json()
    return await u.edit(f"**{resp['quote']}**\n — __{resp['character']} ({resp['anime']})__")
  except:
    await u.edit("`Something went wrong LOL ...`")

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
