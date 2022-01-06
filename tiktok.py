# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available

• `{i}tikdl url`
   `Download url from tiktok.`
"""

from . import ultroid_cmd, async_searcher, json_parser, LOGS
from bs4 import BeautifulSoup as Soup

async def tiktok_download(ult):
    # (c) TeamUltroid
    get_ = await async_searcher(ult)
    So = Soup(get_, "html.parser", from_encoding="utf-8")
    Co = json_parser(So.find("script",id="sigi-persisted-data").text[21:][:-515])
    Item = Co["ItemModule"]
    first_item = list(Item.keys())[0]
    Data = Item[first_item]
    nick_name = Data.get("nickname", "")
    if Data.get("desc"):
        Capt = f"**Description:** `{Data['desc']}`"
    else:
        Capt = ""
    Capt += f"\n**By [{nick_name}](https://tiktok.com/{Data['author']})**"
    Capt += "\n\n**• Powered by Ultroid**"
    return Data.get("video", {}).get("downloadAddr"), Capt


@ultroid_cmd(pattern="tikdl( (.*)|$)")
async def dl_tiktok(ult):
    match = ult.pattern_match.group(1).strip()
    if not match:
        return await ult.eor("`Provide TikTok Url to Download...`")
    msg = await ult.eor("`Processing...`")
    try:
        scr, capt = await tiktok_download(match)
        if not scr:
            return await msg.eor("`Video Download Failed!..`", time=8)
        await ult.client.send_message(ult.chat_id, capt, file=scr, reply_to=event.reply_to_msg_id)
        await msg.delete()
    except Exception as er:
        LOGS.exception(er)
        return await msg.eor(f"**ERROR :** `{er}`", time=8)
