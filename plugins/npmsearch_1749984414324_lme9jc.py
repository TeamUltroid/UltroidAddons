# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.tl.types import InputWebDocument as wb
from telethon.tl.custom import Button
from . import in_pattern, InlinePlugin, async_searcher, asst

__doc__ = f"""
✘ Commands Available -

• `@{asst.username} npm <package_name>`
    Searches for the package on NPM and returns the results.
"""


@in_pattern("npm")
async def search_npm(event):
    try:
        query = event.text.split(maxsplit=1)[1]
    except IndexError:
        await event.answer([], switch_pm="Enter query to search", switch_pm_param="start"
        )
        return
    data = await async_searcher(f"https://registry.npmjs.com/-/v1/search?text={query.replace(' ','+')}&size=7", re_json=True)
    res = []
    for obj in data["objects"]:
        package = obj["package"]
        url = package["links"]["npm"]
        title = package["name"]
        keys = package.get("keywords", [])
        text = f"**[{title}]({package['links'].get('homepage', '')})\n{package['description']}**\n"
        text += f"**Version:** `{package['version']}`\n"
        text += f"**Keywords:** `{','.join(keys)}`"
        res.append(await event.builder.article(
            title=title,
            text=text,
            url=url,
            link_preview=False,
            buttons=[
                Button.url("View", url),
                Button.switch_inline("Search again", query=event.text, same_peer=True),
            ],
        ))
    await event.answer(res, switch_pm="NPM Search", switch_pm_param="start")

InlinePlugin.update({"Npm Search": "npm"})
