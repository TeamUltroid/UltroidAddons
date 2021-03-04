#made by @senku_ishigamiii/@Uzumaki_Naruto_XD

'''
✘ Commands Available
• `{i}transferch (usename to whom you have to transfer channel`
        
"""


import telethon.password as pwd_mod
from telethon.tl import functions


@ultroid_cmd(pattern="transferch (.*)")
async def oof(ult):
    if ult.fwd_from:
        return
    username = ult.pattern_match.group(1)
    current_channel = ult.chat_id
    try:
        pwd = await ult.client(functions.account.GetPasswordRequest())
        my_srp_password = pwd_mod.compute_check(pwd, Config.TELE_GRAM_2FA_CODE)
        await ult.client(
            functions.channels.EditCreatorRequest(
                channel=current_channel, user_id=username, password=my_srp_password
            )
        )
    except Exception as e:
        await ult.edit(str(e))
    else:
        await ult.edit("Transferred 🌚")
        
        
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})

