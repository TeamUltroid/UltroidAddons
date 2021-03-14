#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# .tweet made for ultroid


"""
✘ Commands Available -

• `{i}tweet`
    make twitter posts.

• `{i}quote`
    quote search via @GoodQuoteBot.

"""

import random
from . import *
from telethon.errors import (
    ChatSendInlineForbiddenError,
    ChatSendStickersForbiddenError
    )


@ultroid_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if text is None:
        return await wai.edit('`Give me Some Text !`')
    try:
        results = await ultroid_bot.inline_query(
            "twitterstatusbot", text
        )
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="quote ?(.*)")
async def quote(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    try:
        results = await ultroid_bot.inline_query(
            "goodquotebot",
            text
        )
        if len(results) == 1:
            num = 0
        else:
            num = random.randrange(0, len(results)-1)
        await results[num].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
