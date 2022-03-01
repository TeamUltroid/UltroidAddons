# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


"""
✘ Commands Available

• `{i}imgwhale <Optional<apiKey>>`
    Upload image to https://ImgWhale.xyz !
"""

import requests

@ultroid_cmd(pattern="imgwhale ?(.*)")
async def imgwhale(event):
    msg = await event.eor("`Processing...`")
    api_key = event.pattern_match.group(1)
    # If api_key exists upload with that else do with normal method.
