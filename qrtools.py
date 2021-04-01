#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

• `{i}make <keyword>`
    Make Qr codes of Keyword used.


• `{i}read <replying to Qr Code>`
    Extract/read text of Qr Codes.
"""

import json
import os
import urllib

import requests
from telegraph import upload_file

from . import *


@ultroid_cmd(pattern="make ?(.*)")
async def makeqr(e):
    query = e.pattern_match.group(1)
    if not query:
        return await eor(e, "`Give me some text !`")
    er = await eor(e, "`Making QR Code...`")
    text = urllib.parse.quote(query)
    urllib.request.urlretrieve(
        f"https://api.qrserver.com/v1/create-qr-code/?size=350&data={text}", "qr.png"
    )
    await ultroid_bot.send_file(e.chat_id, "qr.png")
    os.remove("qr.png")
    await er.delete()


@ultroid_cmd(pattern="read$")
async def textify(ult):
    if not ult.is_reply:
        await eor(ult, "`Reply to a Photo...`")
    getr = await ult.get_reply_message()
    msg = await eor(ult, "`Processing...`")
    dfile = await getr.download_media()
    up = upload_file(dfile)
    sin = "https://telegra.ph" + up[0]
    link = urllib.parse.quote(sin)
    getc = requests.get(
        f"http://api.qrserver.com/v1/read-qr-code/?fileurl={link}"
    ).content
    rt = json.loads(getc.decode("utf-8"))
    if not rt[0]["type"] == "qrcode":
        return await msg.edit("Not a Valid Qr-Code")
    dat = rt[0]["symbol"][0]["data"]
    ret = f"**💬 QR To Text**\n\n📃 **OUTPUT :** `{dat}`"
    await msg.edit(ret)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
