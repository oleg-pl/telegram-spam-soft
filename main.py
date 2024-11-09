import os

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
import random
from constants import *
import asyncio
from time import sleep
import requests
import socks

with open("texts.txt", mode="r", encoding='utf-8' ) as text_file:
    data = text_file.readlines()
with open("users.txt", "r") as text_file:
    users = text_file.readlines()
with open("current_user.txt", "r") as text_file:
    i = int(text_file.readline())
per_account = 0
current_account = 0
flood = False
accounts = len(os.listdir('./sessions'))


async def main(receiver):
    await client.connect()
    print("HI", receiver)
    await client.send_message(receiver, data[random.randint(0, len(data) - 1)].replace("\\n", "\n"))
    delay = random.uniform(5, 10)
    await asyncio.sleep(delay)


def parse_proxy(proxy_str):
    if proxy_str == '':
        return None
    login, password = proxy_str.split('@')[0].split(':')
    ip, port = proxy_str.split('@')[1].split(':')
    return socks.SOCKS5, ip, int(port), True, login, password


def change_ip():
    requests.get(changeip_link)
    sleep(random.uniform(15, 25))


while i < len(users):
    if per_account >= messageForAccount or flood:
        client.disconnect()
        current_account += 1
        change_ip()
        per_account = 0
        flood = False
    if current_account >= accounts:
        break
    try:
        print(current_account)
        client = TelegramClient(f"sessions/{current_account}", api_id, api_hash, proxy=parse_proxy(proxy))
        client.loop.run_until_complete(main(users[i]))
    except PeerFloodError:
        print("[!] Got Flood Error from telegram. \n[!] Try later.")
        client.disconnect()
        flood = True
    except Exception as e:
        print(e)
        client.disconnect()
        current_account += 1
        change_ip()
    finally:
        client.disconnect()
    i += 1
    per_account += 1
    with open("current_user.txt", 'w') as file:
        file.write(str(i) + '\n')
print('Task complete!')