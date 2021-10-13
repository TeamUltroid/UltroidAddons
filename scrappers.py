# Ultroid Userbot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
"""

# TODO : Complete Plugin 😴

from . import *
import requests as r
from bs4 import BeautifulSoup as bs

@ultroid_cmd(pattern="shutter ?(.*)")
async def scrap_shutter(event):
  match = event.pattern_match.group(1)
  if not match:
    return await eor(event, "`Give Some text to Search for..`")
  uri = "https://www.shutterstock.com/search/" + match.replace(" ", "+")
  reqs = r.get(uri).content
  bbb = bs(reqs, "html.parser", from_encoding="utf-8")
  ml = bbb.find_all("img", src=re.compile("https://image.shutterstock.com/image-photo"))
  LOGS.info(ml)
    
