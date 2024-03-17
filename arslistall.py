from telethon.tl.types import ChannelParticipantsSearch

@ultroid_cmd(pattern="arslistall$")
async def arslistall(ult):
    if ult.fwd_from:
        return
    unique_users_set = set()
    chat = await ult.get_input_chat()

    # Сбор уникальных actor_id и from_id из сообщений
    async for message in ult.client.iter_messages(chat):
        if message.from_id:
            unique_users_set.add(message.from_id.user_id)
        # Для событий, связанных с пользователями, например, добавлении в группу
        if hasattr(message.action, 'actor_id'):
            unique_users_set.add(message.action.actor_id)

    mentions = "This Are The Unique Members In This Group Based on Interaction"
    # Получение информации о пользователях по уникальным ID
    for user_id in unique_users_set:
        user = await ult.client.get_entity(user_id)
        mentions += f"\n - {user.first_name} ({user_id})"

    await ult.reply(mentions)
    await ult.delete()