# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>

import re
from bs4 import BeautifulSoup as bs
from telethon.tl.types import InputWebDocument as wb
from . import get_string, async_searcher, in_pattern, InlinePlugin, asst

__doc__ = f"""
✘ Commands Available -

• `@{asst.username} xda <query>`
    Searches for the query on XDA Developers and returns the results.
"""

# Inspired by @FindXDaBot

@in_pattern("xda", owner=True)
async def xda_dev(event):
    QUERY = event.text.split(maxsplit=1)
    try:
        query = QUERY[1]
    except IndexError:
        await event.answer(
            [], switch_pm=get_string("instu_3"), switch_pm_param="start"
        )
        return
    le = "https://www.xda-developers.com/search/?q=" + query.replace(" ", "+")
    ct = await async_searcher(le, re_content=True)
    ml = bs(ct, "html.parser", from_encoding="utf-8")
    cards = ml.find_all("div", class_="display-card")
    out = []
    for card in cards:
        # Title and URL
        title_tag = card.find("h5", class_="display-card-title")
        a_tag = title_tag.find("a") if title_tag else None
        title = a_tag.get("title") or a_tag.text.strip() if a_tag else "No Title"
        href = a_tag.get("href") if a_tag else ""
        if href and href.startswith("/"):
            href = "https://www.xda-developers.com" + href

        # Description
        desc_tag = card.find("p", class_="display-card-excerpt")
        desc = desc_tag.text.strip() if desc_tag else ""

        # Thumbnail
        img_tag = card.find("img")
        thumb = img_tag.get("data-img-url") or img_tag.get("src") if img_tag else None
        if thumb:
            thumb = wb(thumb, 0, "image/jpeg", [])

        text = f"[{title}]({href})"
        out.append(
            await event.builder.article(
                title=title, description=desc, url=href, thumb=thumb, text=text
            )
        )
    uppar = "|| XDA Search Results ||" if out else "No Results Found :("
    await event.answer(out, switch_pm=uppar, switch_pm_param="start")


InlinePlugin.update({"Search on XDA": "xda telegram"})