# Ultroid Userbot

# made by member of TeamUltroid

# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""

✘ Commands Available -

• `{i}wiki <search query>``
    Wikipedia search from telegram.

"""

from bs4 import BeautifulSoup as bs
import requests


@ultroid_cmd(pattern="wiki ?(.*)")
async def a(e):
    query = e.pattern_match.group(1)
    if not query:
        return await eor(e,'What you want to search ?')
    query = query.replace(' ','%20')
    link = f"https://en.m.wikipedia.org/wiki/{query}"
    gli = requests.get(link)
    mag = bs(gli.content,'html.parser',from_encoding='utf-8')
    fin = mag.find_all('p')
    try:
        text = fin[1].text
    except:
        return await eor(e,'No results found')
    am = mag.find_all('a','image')
    t = mag.find_all('div','page-heading')
    title= t[0].findNext().text
    wiki = mag.find_all('link',rel='canonical')[0]['href']
    img = "https:"+ am[0].findNext()['src']
    msg = f"**Title** - `{title}`\n\n**Image** - [Click Here]({img})\n\n**Summary** - `{text}`\n\n**Page Link** - {wiki}"
    await bot.send_message(e.chat_id,msg,link_preview=True)
    if e.sender_id==ultroid_bot.uid:
        await e.delete()

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
