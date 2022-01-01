# Made by: @tofik_dn for Ultroid - UserBot

"""
✘ Commands Available -

• `{i}asupan`
   To send random intake video.

• `{i}wibu`
   To send a random wibu video.

• `{i}chika`
   To send a random chikakiku video.
"""

import requests

from . import *


@ultroid_cmd(pattern="asupan ?(.*)")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.eor("`Something went wrong LOL...`")


@ultroid_cmd(pattern="wibu ?(.*)")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.eor("`Something went wrong LOL...`")


@ultroid_cmd(pattern="chika ?(.*)")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.eor("`Something went wrong LOL...`")
