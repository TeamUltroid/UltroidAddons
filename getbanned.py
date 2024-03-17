from telethon.tl.types import ChannelParticipantsKicked as banned

@ultroid_cmd(pattern="getbanned$")
async def getbanned(ult):
    try:
        users = await ultroid_bot.get_participants(ult.chat_id,filter=banned)
    except Exception as e:
        return await eor(ult,f"ERROR - {str(e)}")
    if len(users) > 0 :
        msg=f"**LIST OF BANNED MEMBERS !!**\n\n=>> **TOTAL :** {len(users)}\n"
        for user in users:
            if not user.deleted:
                msg+=f"🛡[{user.first_name}]({user.id})\n"
            else:
                msg += "☠️ Deleted Account\n"
        await eor(ult,msg)
    else:
        await eor(ult,"No Banned Users !!")