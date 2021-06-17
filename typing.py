# (c) Shrimadhav U.K
# aka Spechide
#
# Ported for Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}type <msg>`
    Edits the Message and shows like someone is typing.
"""

import asyncio

from . import *


@ultroid_cmd(pattern="type ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await eor(event, "Give me something to type !")
    shiiinabot = "\u2060"
    for i in range(601):
        shiiinabot += "\u2060"
    try:
        okla = await eor(event, shiiinabot)
    except Exception as e:
        print(str(e))
    typing_symbol = "|"
    previous_text = ""
    await okla.edit(typing_symbol)
    await asyncio.sleep(0.4)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        try:
            await okla.edit(typing_text)
        except Exception as e:
            print(str(e))
        await asyncio.sleep(0.4)
        try:
            await okla.edit(previous_text)
        except Exception as e:
            print(e)
        await asyncio.sleep(0.4)
