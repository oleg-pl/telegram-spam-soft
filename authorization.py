import os
from telethon import TelegramClient
from constants import *

number_new_accounts = int(input("Enter the number of accounts you want to add: "))
old_accounts = len(os.listdir('./sessions'))

for i in range(number_new_accounts):
    client = TelegramClient(f"sessions/{i + old_accounts}", api_id, api_hash)
    async def main():
        me = await client.get_me()
        print(me)
    with client:
        client.loop.run_until_complete(main())
