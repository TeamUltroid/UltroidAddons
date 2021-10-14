from . import *


@asst.on(events.ChatAction(func=lambda x: x.user_joined, chats=["ultroidpluginschat"]))
async def hhh(e):
    m = await e.get_sender()
    a = await e.client.kick_participant(e.chat_id, m.id)
    await e.delete()
    await a.delete()
