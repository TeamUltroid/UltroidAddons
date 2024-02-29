
#inspired yet again from dc and written by @Naruto_Uzumaki_Xd/@Senku_ishigamiii


import logging
import queue

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import asyncio
logger = logging.getLogger(__name__)



if 1 == 1:
    name = "Profile Photos"
    client = borg

    @ultroid_cmd(pattern="poto ?(.*)")
    async def potocmd(ult):
        id = "".join(ult.raw_text.split(maxsplit=2)[1:])
        user = await ult.get_reply_message()
        chat = ult.input_chat
        if user:
            photos = await ult.client.get_profile_photos(user.sender)
            u = True
        else:
            photos = await ult.client.get_profile_photos(chat)
            u = False
        if id.strip() == "":
            if len(photos) > 0:
                await ult.client.send_file(ult.chat_id, photos)
            else:
                try:
                    if u is True:
                        photo = await ult.client.download_profile_photo(user.sender)
                    else:
                        photo = await ult.client.download_profile_photo(ult.input_chat)
                    await ult.client.send_file(ult.chat_id, photo)
                except:
                    await ult.edit("**This user has no photos.**")
                    return
        else:
            try:
                id = int(id)
                if id <= 0:
                    await ult.edit("```ID number Invalid Bruh!```")
                    return
            except:
                 await ult.edit("`Are you comedy me ?`")
                 return
            if int(id) <= (len(photos)):
                send_photos = await ult.client.download_media(photos[id - 1])
                await ult.client.send_file(ult.chat_id, send_photos)
            else:
                await ult.edit("```No photo found!```")
                await asyncio.sleep(8)
                return
