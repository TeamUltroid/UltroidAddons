# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
Fasly Bot Cheat.

Use `{i}setdb FASTLY True` to turn this on.
The bot would auto reply first to the messages by @FastlyWriteBot and @FastlyWriteCloneBot.
"""

from . import async_searcher
from telegraph import upload_file
from telethon import events
from . import udB

base_url = "https://api.ocr.space/parse/imageurl?apikey={api}&url={tgraph}"


@ultroid_bot.on(events.NewMessage(incoming=True, from_users=[1806208310, 1983714367]))
async def fastly_bot(event):
    if udB.get("FASTLY") != "True":
        return
    api = udB.get("OCR_API")
    if not api:
        return
    if not event.media and not event.media.photo:
      return
    med = await event.download_media()
    upload = upload_file(med)
    link = "https://telegra.ph" + upload[0]
    out = await async_searcher(base_url.format(api=api, tgraph=link), re_json=True)
    try:
        txt = out["ParsedResults"][0]["ParsedText"]
    except:
        return
    txt = txt.replace("By@FastlyWriteBot", "").replace("\n", "").replace("\r", "")
    if txt:
        try:
            await event.reply(txt)
        except:
            return
