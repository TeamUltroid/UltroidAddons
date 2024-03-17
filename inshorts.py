from . import *
from . import asst

f"""
Inshorts Search 

-> Inline Plugin
`@{asst.me.username} inshorts`
"""


from telethon.tl.types import InputWebDocument as wb
from bs4 import BeautifulSoup as bs

@in_pattern(pattern="inshorts", owner=True)
async def get_news(event):
  url = "https://www.inshorts.com/en/read"
  _ = await async_searcher(url, re_content=True)
  bsC = bs(_, "html.parser", from_encoding="utf-8")
  boxes = bsC.find_all("div", "news-card")
  res = []
  for box in boxes:
    title = box.find("span", itemprop="headline").text
    by_ = box.find("span", "author").text
    img = box.find("meta", itemprop="url")["content"]
    text = f"• **{title}**\n__By {by_}__\n\n"
    text += "__" + box.find("div", itemprop="articleBody").text + "__"
    iwb = wb(img, 0, "image/jpeg", [])
    url = "https://inshorts.com" + box.find("a", "clickable", href=re.compile("en/news"))["href"]
    text += f"\n\n• [View on Inshorts]({url}) •"
    res.append(await event.builder.article(title=title, type="photo",
    url=url, description="By :" + by_, text=text,
    thumb=iwb, content=iwb, include_media=True))
  await event.answer(res, switch_pm="Ultroid@InShorts.com on Telegram", switch_pm_param="start")