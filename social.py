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
"""

@ultroid_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wait = eor(e,"processing...")
    text = e.pattern_match.group(1)
    try:
        results = await ultroid_bot.inline_query(
            "twitterstatusbot",text
        )
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wait.delete()
    except ChatSendInlineForbiddenError:
        await wait.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wait.edit("Sorry boss, I can't send Sticker Here !!")
