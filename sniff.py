# Sniff Config By Dappzx
# Ported to ultroid by eris 
# Ported for Ultroid < https://github.com/TeamUltroid/Ultroid >

✘ Commands Available -
• `{i}sniff <upper text> ; <lower text> <reply to File>`
    To Decrypt Config,

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
	user = await bot.get_me()
	if not user.username:
		uname = user.first_name
	uname = user.username
	reply = await e.get_reply_message()
	if not (reply and reply.media):
		await eor(e, "Reply to a File’")
		return
	eris = await eor(e, "`Processing...`")
	ERROR_ = "Unblok bot @hcdecryptor_bot untuk menggunakan command ini"
	chat = await ultroid_bot.get_entity(chat)
	async with ultroid_bot.conversation(chat.username, timeout=15) as conv:
		try: 
			response = conv.wait_event(events.NewMessage(incoming=True, from_users=chat.id))
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
		if "Satisfied with the result" in msg:
			msg = msg.replace("Satisfied with the result? Follow us!","").replace("🌐 BOT CHANNEL: @hctoolschannel","").replace("🌐 BOT GROUP: @hctools","").replace("💻 SOURCE CODE: https://github.com/hctools/hcdrill-tg","")
			msg = f"Dec by: @{uname}\n\n{msg}"
			await eris.respond(msg, link_preview=False)
			await eris.delete()
			await ultroid_bot.send_read_acknowledge(chat.id)
