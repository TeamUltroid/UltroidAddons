#credits to @Harpia-Vieillot
#For @TeamUltroid
'''
✘ Commands Available
• `{i}wreplace <count> <old word>;<new word>`
    Note : Don't use brackets\n\nEx. : {i}replace 10;Hi;Hello\n\nUse: It replaces a perticular word by new word (only in your msgs.) In many msgs at a time
'''
from . import *
import time
@ultroid_cmd(pattern="wreplace")
async def harpia(e):
  sed = str(e.text[10:])
  lst = sed.split(" ", 1)
  lmt = int(lst[0]) + 1
  s = lst[1]
  pist = s.split(";")
  async for x in bot.iter_messages(e.chat_id, limit= lmt, from_user="me"):
  	msg = x.text
  	if pist[0] in msg:
  	 m = msg.replace(pist[0], pist[1])
  	 await x.edit(m)
  await e.edit("Finished...")
  time.sleep(5)
  await e.delete()

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
