# updated by @nub_a_f
# previously @senku_ishigamiii/ @Uzumaki_Naruto_XD
# that can only check client/owner's limitations
# but now can check anyone's limitations

"""
✘ Commands Available -

• `{i}limited`
   Check you/anyone are limited or not !

"""

from . import *

@ultroid_cmd(pattern="limited$")
async def _(e):
   msg = await eor(e, "checking if you are limited or not...")
   if e.reply_to_msg_id:
     reply = await e.get_reply_message()
     lel = await ultroid_bot.get_entity(reply.sender_id)
     x = lel.restriction_reason
     if x:
       await msg.edit(f"`{x}`")
     else: 
       await msg.edit(f"Good news, no limits are currently applied to {reply.sender.first_name}'s account. {reply.sender.first_name} is free as a bird!")
   else: 
     xx = ultroid_bot.me.restriction_reason
     if xx:
       await msg.edit(f"`{xx}`")
     else:
       await msg.edit("Good news, no limits are currently applied to your account. You’re free as a bird!")
     
