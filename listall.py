@ultroid_cmd(pattern="listall")
async def listall(ult):
    if ult.fwd_from:
        return
    mentions = "This Are The Members In This Group"
    chat = await ult.get_input_chat()
    async for x in borg.iter_participants(chat, 10000):
        mentions += f" \n {x.first_name}"
    await ult.reply(mentions)
    await ult.delete()
    
    #code written by @senku_ishigamiii 
