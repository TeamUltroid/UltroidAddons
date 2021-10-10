# updated by @nub_a_f
# previously @senku_ishigamiii/ @Uzumaki_Naruto_XD
# that can only check client/owner's limitations
# but now can check anyone's limitations

"""
✘ Commands Available -

• `{i}limited`
   Check restrictions on someone/self account!

"""

from . import *


@ultroid_cmd(pattern="limited ?(.*)")
async def _(e):
    match = e.pattern_match.group(1)
    msg = await eor(e, "checking if account is limited or not...")
    if match:
        lel = match
    elif e.reply_to_msg_id:
        reply = await e.get_reply_message()
        lel = reply.sender_id
    else:
        lel = "me"
    pro = await e.client.get_entity(lel)
    rest = pro.restriction_reason
    if rest:
        xx = f"Restriction on {get_display_name(pro)}\n".join(
            f"\n• `{a}`" for a in rest
        )
        return await msg.edit(xx)
    return await msg.edit(
        "`Good news, no limits are currently applied to account. You’re free as a bird!`"
    )
