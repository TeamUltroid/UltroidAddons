# Coded by t.me/Fusuf #
# Please ask before kang #
# 2020 @AsenaUserBot #

# Ported for Ultroid

from requests import get
from os import remove
from telegraph import upload_file as uplu
from . import *

@ultroid_cmd(pattern="ptrigger$")
async def ptrigger(event):
    if not event.is_reply:
        return await event.edit('**Reply to a Message!**')
    msg = await eor(event, "`Processing...`")
    reply = await event.get_reply_message()
    foto = await ultroid_bot.download_profile_photo(reply.from_id.user_id)
    if foto == None:
        return await msg.edit("`Replied User dont have Profile Photo !`")
    avatar = uplu(foto)
    r = get(f"https://some-random-api.ml/canvas/triggered?avatar=https://telegra.ph{avatar[0]}", allow_redirects=True)
    open('triggered.gif', 'wb').write(r.content)
    await ultroid_bot.send_file(event.chat_id, "triggered.gif", caption="**Trigerred**", reply_to=reply)
    await msg.delete()
    remove(foto)
    remove("triggered.gif")