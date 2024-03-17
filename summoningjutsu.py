#credit to @senku_ishigamiii/@Naruto_Uzumaki_XD
import asyncio
from . import *


@ultroid_cmd(pattern="summoningjutsu")
async def summon(ult):
 ult.delete()
 a = await ult.client.send_file(ult.chat_id, "CAADBQADEwIAAkceYVabauGjzQ4OUgI")
 await asyncio.sleep(1)
 await a.delete()
 e = await ult.client.send_file(ult.chat_id, "CAADBQADeQMAAj28YFb0CAvlSjuV5gI")
 await asyncio.sleep(1)
 await e.delete()
 b = await ult.client.send_file(ult.chat_id, "CAADBQADPwIAAlyRYVamvYbqTt3XjQI")
 await asyncio.sleep(1)
 await b.delete()
 c = await ult.client.send_file(ult.chat_id, "CAADBQADlAIAAnW1WVaorC7sMkfgKQI")
 await asyncio.sleep(1)
 await c.delete()
 d = await ult.client.send_file(ult.chat_id, "CAADAgADXwAD9PRuFwpjuaddBSAcAg")
 await asyncio.sleep(1)
 await d.delete()
 f = await ult.client.send_file(ult.chat_id, "CAADBQADdgIAAg62YVZOh1Z4kDVrfQI")
 await asyncio.sleep(1)
 await f.delete()
 await asyncio.sleep(1)
 await ult.respond("summoning jutsu!!!!!!!!!")
 ult.delete()
 await ult.client.send_file(ult.chat_id, "https://telegra.ph/file/78c05f1d42e16c61990ca.jpg")