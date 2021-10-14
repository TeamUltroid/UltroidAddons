# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


"""
✘ Commands Available

• `{i}freepik <query> ; limit`
    search images on freepik.
"""

from . import *
from random import shuffle
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

@ultroid_cmd(pattern="freepik ?(.*)")
async def fnew_pik(event):
  match = event.pattern_match.group(1)
  limit = 5
  if not match:
    return await eor(event, "`Give Something to Search!`")
  if " ; " in match:
    _ = match.split(" ", maxsplit=1)
    match = _[0]
    limit = int(_[1])
  content = urlopen(f"https://www.freepik.com/search?format=search&page=1&query={match}")
  reso = bs(a, "html.parser", from_encoding="utf-8")
  con = reso.find_all("img", src=re.compile("img.freepik.com"))
  if not con:
    return await eor(event, "No Results Found!")
  shuffle(con)
  lml = [a["src"] for a in con[:limit]]
  await event.client.send_message(event.chat_id, f"Uploaded {len(lml)} Images!", file=lml)
  await event.delete()
