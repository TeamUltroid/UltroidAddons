# credit https://t.me/I_m_FlaSh

"""
✘ Commands Available -
• `{i}totalmsgs`
    Returns your total msg count in current chat
    
• `{i}totalmsgs [username]`
    Returns total msg count of user in current chat
"""

from . import *

@ultroid_cmd(pattern="totalmsgs ?(.*)")
async def _(e):
  k = await e.get_reply_message()
  if k :
      a = await ultroid_bot.get_messages(e.chat_id, 0, from_user=k.sender_id)
      return await eor(e, f"Total msgs of {u} here = {a.total}")
  u = e.pattern_match.group(1)
  if not u:
    u = "me"
  a = await ultroid_bot.get_messages(e.chat_id, 0, from_user=u)
  await eor(e, f"Total msgs of {u} here = {a.total}")
  

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})  
