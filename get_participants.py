from telethon import TelegramClient
from constants import *
import asyncio


async def get_members():
    return await client.get_participants('whitecryptonchat')

if __name__ == '__main__':

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient(f"sessions/0", api_id, api_hash, loop=loop)

    with client:
        members = client.loop.run_until_complete(get_members())
    member = members[0]
    with open("users.txt", 'w') as file:
        for member in members:
            try:
                file.write(member.username + '\n')
            except Exception as error:
                print(f"{member.id} doesn't have a username")
    with open("current_user.txt", 'w') as file:
        file.write('0' + '\n')