# Ultroid Userbot

# Ported from @UserbotPlugins
# originally from jeepbot for uniborg

"""
Search movie details from IMDB

✘ Commands Available
• `{i}imdb <keyword>`
"""

import re

import bs4
import requests

from . import *

langi = "en"


@ultroid_cmd(pattern="imdb ?(.*)")
async def imdb(e):
    await eor(e, "`...`")
    movie_name = e.pattern_match.group(1)
    if not movie_name:
        return await eor(e, "`Provide a movie name too`")
    try:
        await eor(e, "`Processing...`")
        remove_space = movie_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all"
        )
        soup = bs4.BeautifulSoup(page.content, "lxml")
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext("td").findNext("td").text
        mov_link = (
            "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
        )
        page1 = requests.get(mov_link)
        soup = bs4.BeautifulSoup(page1.content, "lxml")
        if soup.find("div", "title_wrapper"):
            pg = soup.find("div", "title_wrapper").findNext("div").text
            mov_details = re.sub(r"\s+", " ", pg)
        else:
            mov_details = ""
        credits = soup.findAll("div", "credit_summary_item")
        if len(credits) == 1:
            director = credits[0].a.text
            writer = "Not available"
            stars = "Not available"
        elif len(credits) > 2:
            director = credits[0].a.text
            writer = credits[1].a.text
            actors = []
            for x in credits[2].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        else:
            director = credits[0].a.text
            writer = "Not available"
            actors = []
            for x in credits[1].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        if soup.find("div", "inline canwrap"):
            story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
        else:
            story_line = "Not available"
        info = soup.findAll("div", "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll("a")
                for i in a:
                    if "country_of_origin" in i["href"]:
                        mov_country.append(i.text)
                    elif "primary_language" in i["href"]:
                        mov_language.append(i.text)
        if soup.findAll("div", "ratingValue"):
            for r in soup.findAll("div", "ratingValue"):
                mov_rating = r.strong["title"]
        else:
            mov_rating = "Not available"

        return await eor(
            e,
            f"**Title :** `{mov_title}`\n"
            + f"`{mov_details}`\n"
            + f"**Rating :** `{mov_rating}`\n"
            + f"**Country :** `{mov_country[0]}`\n"
            + f"**Language :** `{mov_language[0]}`\n"
            + f"**Director :** `{director}`\n"
            + f"**Writer :** `{writer}`\n"
            + f"**Stars :** `{stars}`\n"
            + f"**IMDB Url :** {mov_link}\n"
            + f"**Story Line :** `{story_line}`",
        )
    except IndexError:
        return await eor(e, "Something went wrong ...")
