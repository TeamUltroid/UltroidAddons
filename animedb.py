# Made by : @Arnab431 || github.com/ArnabXD
# Made For : https://github.com/TeamUltroid/UltroidAddons

"""
Search animes and manga from anilist.co using @animedb_bot

✘ Commands Available
• `{i}anime <keyword>`
    To get anime info
• `{i}manga <keyword>`
    To get manga info
"""

from . import HELP
from telethon.errors import ChatSendInlineForbiddenError

@ultroid_cmd(
    pattern="anime ?(.*)",
)
async def anime(ult):
    await ult.edit("`Searching ...`")
    keyword = ult.pattern_match.group(1)
    if keyword is None:
        return await ult.edit("`Provide a Keyword to search`")
    try:
        animes = await ultroid_bot.inline_query("animedb_bot", keyword)
        await animes[0].click(
            ult.chat_id,
            reply_to=ult.reply_to_msg_id,
            silent=True if ult.is_reply else False,
            hide_via=True,
        )
        return await ult.delete()
    except ChatSendInlineForbiddenError:
        return await ult.edit("`Seems like inline messages aren't allowed here`")
    except:
        return await ult.edit("`No Results Found ...`")


@ultroid_cmd(
    pattern="manga ?(.*)",
)
async def anime(ult):
    await ult.edit("`Searching ...`")
    keyword = ult.pattern_match.group(1)
    if keyword is None:
        return await ult.edit("`Provide a Keyword to search`")
    try:
        animes = await ultroid_bot.inline_query("animedb_bot", f"<m> {keyword}")
        await animes[0].click(
            ult.chat_id,
            reply_to=ult.reply_to_msg_id,
            silent=True if ult.is_reply else False,
            hide_via=True,
        )
        return await ult.delete()
    except ChatSendInlineForbiddenError:
        return await ult.edit("`Seems like inline messages aren't allowed here`")
    except:
        return await ult.edit("`No Results Found ...`")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
