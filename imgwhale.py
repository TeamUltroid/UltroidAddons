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
from . import *


@ultroid_cmd(pattern="imgwhale")
async def imgwhale(event):
    msg = await event.eor("`Processing...`")
    reply = await event.get_reply_message()
    if not reply:
        return await msg.edit("`Reply to Image...`")
    if reply.photo:
        file = await reply.download_media()
    elif reply.document and reply.document.thumbs:
        file = await reply.download_media(thumb=-1)
    else:
        return await msg.edit("`Reply to Image...`")
    api_key = udB.get_key("IMGWHALE_KEY")
    json = {}
    if api_key:
        json.update({"key":api_key})
    post = await async_searcher("https://imgwhale.xyz/new", post=True, data={'image': open(file, 'rb')} ,json=json, re_json=True)
    if post.get("error"):
        return await msg.edit(post["message"])
    await msg.edit(f"Successfully Uploaded to [ImhWhale](https://imgwhale.xyz/{post['fileId']})")