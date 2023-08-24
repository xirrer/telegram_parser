import configparser
import json

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)

client.start()


async def dump_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0
    limit_msg = 100

    all_messages = []

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None, add_offset=0,
            limit=limit_msg, max_id=0, min_id=0,
            hash=0))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            if message.message:
                sender_name = sender.first_name if hasattr(message.from_id, 'username') else "N/A"
                all_messages.append({"sender": sender_name, "message": message.message})
        offset_msg = messages[len(messages) - 1].id

    with open('channel_messages.json', 'w', encoding='utf8') as outfile:
        for message in all_messages:
            outfile.write('Sender: ' + message["sender"] + '\n')
            outfile.write('Message: ' + message["message"] + '\n\n')



async def dump_all_participants(channel):
    """Записываем json-файл с информацией о всех участниках канала/чата. . ."""
    offset_user = 0
    limit_user = 100

    all_participants = []
    filter_user = ChannelParticipantsSearch('')

    while True:
        participants = await client(GetParticipantsRequest(channel,
            filter_user, offset_user, limit_user, hash=0))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    all_users_details = []  

    for participant in all_participants:
        all_users_details.append({"id": participant.id,
                                  "first_name": participant.first_name,
                                  "last_name": participant.last_name,
                                  "user": participant.username,
                                  "phone": participant.phone,
                                  "is_bot": participant.bot})

    with open('channel_users.json', 'w', encoding='utf8') as outfile:
        for user_details in all_users_details:
            json.dump(user_details, outfile, ensure_ascii=False)
            outfile.write('\n') 



async def main():
    url = input("Введите ссылку на канал или чат: ")
    channel = await client.get_entity(url)
    await dump_all_messages(channel)


with client:
    client.loop.run_until_complete(main())
