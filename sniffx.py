"Sniff CFG by Dappzx"
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#sniff
@userge.on_cmd("sniff", about={
	'header': "SNIFF",
	'usage': "{tr}sniff [Reply ke cfg]\n"})
	
async def gen(message: Message):
	"""Untuk sniff config"""
	user = await userge.get_me()
	uname = user.username
	replied = message.reply_to_message
	chat = "@hcdecryptor_bot"
	await message.edit("```Wait for result... ```")
	msgs = []
	ERROR_MSG = "Unblok bot @hcdecryptor_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.forward_message(replied)
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Satisfied with the result" in msgs.text:
				msgs = msgs.text.replace("Satisfied with the result? Follow us!","").replace("🌐 BOT CHANNEL: @hctoolschannel","").replace("🌐 BOT GROUP: @hctools","").replace("💻 SOURCE CODE: https://github.com/hctools/hcdrill-tg","")
				msgs = f"Dec by: @{uname}\n\n{msgs}".replace("[>]","•")
			else:
				msgs = msgs.text
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)