@ultroid_cmd(pattern="tagall")
async def tagall(ult):
    if ult.fwd_from:
        return
    mentions = "Hey there!"
    chat = await ult.get_input_chat()
    async for x in borg.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await ult.reply(mentions)
    await ult.delete()
    
    #code written by @senku_ishigamiii and inspired from @xditya 
