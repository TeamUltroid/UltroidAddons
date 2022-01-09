# Ultroid - UserBot
# Copyright (C) 2022 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -
• `{i}gist <text / reply> Include long text / Reply to text.`
"""

from . import *
from github3 import create_gist


@ultroid_cmd(pattern="gist( (.*)|$)", manager=True, allow_all=True)
async def _(event):
    # creating anonymous gist , i will add document support soon
    try:
        input_str = event.text.split(maxsplit=1)[1]
    except IndexError:
        input_str = None
    xx = await event.eor("` 《 Pasting on gist... 》 `")
    if input_str:
        message = input_str
    elif event.reply_to:
        reply = await event.get_reply_message()
        if reply.text:
            message = reply
    else:
        message = None
    if not message:
        return await xx.eor(
            "`Reply to a Message or Give me Some Text !`", time=5
        )
    try:
        file = {
            'ultroid.txt' : {
                'content': message
            }
        }
        gist = create_gist("ultroid", file)
        link = gist.html_url
        reply_text = f"• **Pasted to Gist :** [gist]({link})"
        await xx.eor(reply_text)
    except Exception as ul:
        LOGS.info(str(ul))
