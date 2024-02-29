# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#Edited By @Senku_Ishigamiii from autowaifu plugin
"""
✘ Commands Available -

•{i} .autohusbando on/off
  This auto show result for @Collect_your_husbando_bot
  
"""
import os
import requests
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from . import *
XX = "A husbando appeared!"

@ultroid_cmd(pattern="autohusbando ?(.*)")
async def _(e): 
    args = e.pattern_match.group(1)
    uff = await eor(e,"Processing...")
    if args:
        if args == "on":
            udB.set("HUSBANDO","TRUE")
            return await uff.edit("AutoHusbando - ON")
        if args == "off":
            udB.set("HUSBANDO","FALSE")
            return await uff.edit("AutoHusbando - OFF")

    husbando = udB.get("HUSBANDO")
    status = "ON" if husbando == "TRUE" else "OFF"
    return await uff.edit(f"AutoHusbando - {status}")

@ultroid_bot.on(events.NewMessage(incoming=True))
async def reverse(event):
    if not event.media:
        return
    if not XX in event.text:
        return
    if not event.sender_id == 1964681186:
        return
    if Redis("HUSBANDO")!="TRUE":
        return
    dl = await ultroid_bot.download_media(event.media, "resources/")
    file = {"encoded_image": (dl, open(dl, "rb"))}
    grs = requests.post(
        "https://www.google.com/searchbyimage/upload", files=file, allow_redirects=False
    )
    loc = grs.headers.get("Location")
    response = requests.get(
        loc,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        },
    )
    xx = bs(response.text, "html.parser")
    div = xx.find_all("div", {"class": "r5a77d"})[0]
    alls = div.find("a")
    text = alls.text
    send = await ultroid_bot.send_message(event.chat_id, f"/protecc {text}")
    await sleep(2)
    await send.delete()
    os.remove(dl)
    
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})