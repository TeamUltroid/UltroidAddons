from telethon.tl.types import ChannelParticipantsAdmins as admin

@ultroid_cmd(pattern="demall$")
async def err(e):
    sr = await ultroid_bot.get_participants(e.chat.id,filter=admin)
    et = 0
    for i in sr:
        try:
            await ultroid_bot.edit_admin(e.chat.id,i.id,change_info=False,delete_messages=False,ban_users=False,invite_users=False,manage_call=False,add_admins=False,anonymous=False)
            et += 1
        except Exception as r: await eor(e,str(r))
    await eor(e,f"Demoted {et} admins !")