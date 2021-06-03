# Credits @Dappzx & Ported by Eris
# Base on Userge
# Ported for Ultroid < https://github.com/TeamUltroid/Ultroid >   

from asyncio import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from . import *


@ultroid_cmd(pattern="sniff$")
async def gen(e):
    if e.fwd_from:
        return
    chat = "@hcdecryptor_bot"
    reply = await e.get_reply_message()
    if not (reply and reply.media):
        await eor(e, "Reply to a File’")
        return
    eris = await eor(e, "`Processing...`")
    ERROR_ = "Unblok bot @hcdecryptor_bot untuk menggunakan command ini"
    chat = await ultroid_bot.get_entity(chat)
    async with ultroid_bot.conversation(chat.username, timeout=15) as conv:
        try: 
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=chat.id)
            )
            await reply.forward_to(chat.username)
            response = await response
        except YouBlockedUserError:
            await eris.edit(f"`{ERROR_}`")
            return
        except asyncio.TimeoutError:
            return await eris.edit("`Bot didn't respond in time`")
        except Exception as ex:
            return await eris.edit(f"Error: `{ex}`")

        msg = response.message.message
        await eris.respond(msg, link_preview=False)
        await eris.delete()
        await ultroid_bot.send_read_acknowledge(chat.id)
