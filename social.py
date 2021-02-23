#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# .tweet made for ultroid

# .youtube orginally by Fusuf and small edits by @KarbonCopy
# Coded by t.me/Fusuf #
# 2020 @AsenaUserBot #


"""
✘ Commands Available -

• `{i}tweet`
    make twitter posts.

• `{i}youtube`
    comment on video.
"""

from . import *
from urllib.parse import quote
from requests import get
from telegraph import upload_file
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError


@ultroid_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wai = await eor(e,"processing...")
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
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="youtube")
async def yutup(event):
    if not event.is_reply:
        return await eor(event, "**Reply to a message!**")
    if not event.text:
        return await eor(event, "**Please reply to a Text Message!**")
    if len(event.text) > 30:
        return await eor(event,"`Thats Really a Long Text, Try with smaller...`")
    msg = await eor(event, "`Commenting On Youtube \nwait a while....`")
    reply = await event.get_reply_message()
    foto = await ultroid_bot.download_profile_photo(reply.sender_id)
    whyu = await ultroid_bot(GetFullUserRequest(reply.sender_id))
    username = whyu.user.first_name
    username = username.replace(" ","%20")
    plun=""
    if foto is None:
        plun= "https://www.cybersmile.org/wp-content/plugins/cybersmile-forum//style/default-avatar.png"
    else:
        avatar = upload_file(foto)
        plun = f"https://telegra.ph{avatar[0]}"
    json = f"https://some-random-api.ml/canvas/youtube-comment?avatar={plun}&comment={quote(reply.message)}&username={username}"
    r = get(json, allow_redirects=True)
    open("youtube.png", "wb").write(r.content)
    await ultroid_bot.send_file(
        event.chat_id,
        "youtube.png",
        reply_to=reply,
    )
    await msg.delete()
    remove(foto)
    remove("youtube.png")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
