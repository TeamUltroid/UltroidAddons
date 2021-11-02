# Ultroid Userbot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

• `horo sign`
  `Get Horoscope for Today..`
"""

from . import *


@ultroid_cmd(pattern="horo ?(.*)")
async def hhhh(eve):
    match = eve.pattern_match.group(1)
    if not match:
        return await eor(eve, "`Provide your sign to get Your Horoscope..`")
    data = await async_searcher(f"https://aztro.sameerkumar.website/?sign={match}&day=today", post=True, re_json=True)
    if data.get("message"):
        return await eor(eve, f"**ERROR :** `{data.get('message').split('.')[0]}`")
    msg = ""
    for key in data.keys():
        _key = key[0].upper() + key[1:]
        msg += f"• **{_key.replace('_', ' ')}** : `{data[key]}`\n"
    await eor(eve, msg)
