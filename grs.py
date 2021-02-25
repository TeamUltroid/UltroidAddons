# Ultroid Userbot 
# Copyright 2020 (c)

# ported for ultroid from @userbotplugin

# Google Reverse Search


import requests
from bs4 import BeautifulSoup

@ultroid_cmd(pattern="egrs")
async def grs(e):
    if not e.is_reply:
        return await eor(e,'Reply to a Message')
    msg = await e.get_reply_message()
    if not (msg.media or msg.media.photo):
        return await eor (e,'Reply to a photo')
    file = await msg.download_media()
    BASE_URL = "http://www.google.com"
    URL = "http://www.google.com/searchbyimage/upload"
    a = await eor(e,'Processing...')
    multipart = {
                "encoded_image": (file, open(file, "rb")),
                "image_content": ""
            }
    response = requests.post(URL, files=multipart, allow_redirects=False)
    location = response.headers.get("Location")
    ab = await a.edit("Found Google Result. Pouring some soup on it!")
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
    response = requests.get(location, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
    prs_anchor_element = prs_div.find("a")
    prs_url = BASE_URL + prs_anchor_element.get("href")
    prs_text = prs_anchor_element.text
    # document.getElementById("jHnbRc")
    img_size_div = soup.find(id="jHnbRc")
    img_size = img_size_div.find_all("div")
    OUTPUT_STR = f"""{img_size}
<b>Possible Related Search</b> : <a href="{prs_url}">{prs_text}</a>
<b>More Info</b>: Open this <a href="{location}">Link</a> ."""
    await a.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)
