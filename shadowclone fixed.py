#credit to @senku_ishigamiii/@Naruto_Uzumaki_XD/@testingpluginnn

import asyncio
from . import *
from userbot import ultroid_cmd



@ultroid_cmd(pattern="shadowclone$")
async def summon(ult):
  ult.delete()
  a = await ult.client.send_file(ult.chat_id, "CAADBQADTQQAAjIGoVZ7OvJtD0u3gwI")
  await asyncio.sleep(1.5)
  await a.delete()

  e = await ult.client.send_file(ult.chat_id, "CAADBQADgQIAAv0HqVYf8g-XlFYo2gI")
  await asyncio.sleep(1.5)
  await e.delete()

  b = await ult.client.send_file(ult.chat_id, "CAADBQADiQUAAj_woFaF8Va36nUjUgI")
  await asyncio.sleep(1.5)
  await b.delete()

  c = await ult.client.send_file(ult.chat_id, "CAADBQADBgIAAi7IoVasfvifJ20FwQI")
  await asyncio.sleep(1.5)
  await c.delete()

  d = await ult.client.send_file(ult.chat_id, "CAADBQADKQIAAuqfoVY1KwWWaeAb8QI")
  await asyncio.sleep(1.5)
  await d.delete()

  await asyncio.sleep(1)
  await ult.respond("Shadow Clone Jutsu!!")
  await ult.delete()
  await ult.client.send_file(ult.chat_id, "https://telegra.ph/file/2d5c219f6147e5fc59a89.jpg")