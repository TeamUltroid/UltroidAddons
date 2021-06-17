# Ported From DarkCobra , Originally By Uniborg
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


"""
✘ Commands Available

• `{i}clone <reply/username>`
    clone the identity of user.

• `{i}revert`
    Revert to your original identity

"""

import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          UploadProfilePhotoRequest)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from . import *


@ultroid_cmd(pattern="clone ?(.*)")
async def _(event):
    eve = await eor(event, "`Processing...`")
    reply_message = await event.get_reply_message()
    whoiam = await ultroid_bot(GetFullUserRequest(ultroid_bot.uid))
    if whoiam.about:
        mybio = str(ultroid_bot.me.id) + "01"
        udB.set(f"{mybio}", whoiam.about)  # saving bio for revert
    udB.set(f"{ultroid_bot.uid}02", whoiam.user.first_name)
    if whoiam.user.last_name:
        udB.set(f"{ultroid_bot.uid}03", whoiam.user.last_name)
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await eve.edit(str(error_i_a))
        return
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(user_id)
    first_name = html.escape(replied_user.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮"
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await ultroid_bot(UpdateProfileRequest(first_name=first_name))
    await ultroid_bot(UpdateProfileRequest(last_name=last_name))
    await ultroid_bot(UpdateProfileRequest(about=user_bio))
    pfile = await ultroid_bot.upload_file(profile_pic)  # pylint:disable=E060
    await ultroid_bot(UploadProfilePhotoRequest(pfile))
    await eve.delete()
    await ultroid_bot.send_message(
        event.chat_id, f"**I am `{first_name}` from now...**", reply_to=reply_message
    )


@ultroid_cmd(pattern="revert$")
async def _(event):
    name = OWNER_NAME
    ok = ""
    mybio = str(ultroid_bot.me.id) + "01"
    bio = "Error : Bio Lost"
    chc = udB.get(mybio)
    if chc:
        bio = chc
    fname = udB.get(f"{ultroid_bot.uid}02")
    lname = udB.get(f"{ultroid_bot.uid}03")
    if fname:
        name = fname
    if lname:
        ok = lname
    n = 1
    await ultroid_bot(
        DeletePhotosRequest(await event.client.get_profile_photos("me", limit=n))
    )
    await ultroid_bot(UpdateProfileRequest(about=bio))
    await ultroid_bot(UpdateProfileRequest(first_name=name))
    await ultroid_bot(UpdateProfileRequest(last_name=ok))
    await eor(event, "Succesfully reverted to your account back !")
    udB.delete(f"{ultroid_bot.uid}01")
    udB.delete(f"{ultroid_bot.uid}02")
    udB.delete(f"{ultroid_bot.uid}03")


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.sender_id
                    or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
