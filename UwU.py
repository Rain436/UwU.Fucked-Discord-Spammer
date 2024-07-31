import time
import os

from discord_webhook import DiscordWebhook
from colorama import Fore, Back, Style, init

## Bad Code LOL

Logo = """                                   
 _____       _____   _____         _         _ 
|  |  |_ _ _|  |  | |   __|_ _ ___| |_ ___ _| |
|  |  | | | |  |  |_|   __| | |  _| '_| -_| . |
|_____|_____|_____|_|__|  |___|___|_,_|___|___|
                                               
"""

def webhooksendevent():
    webhook = DiscordWebhook(url=f"{discordWebhook}", content=f"@here {discordcon} - UwU.Fucked")
    response = webhook.execute()
os.system("title- UwU.Fucked - Webhook Fucker - & cls")
print(f""""{Fore.LIGHTMAGENTA_EX}                                   
 _____       _____   _____         _         _ 
|  |  |_ _ _|  |  | |   __|_ _ ___| |_ ___ _| |
|  |  | | | |  |  |_|   __| | |  _| '_| -_| . |
|_____|_____|_____|_|__|  |___|___|_,_|___|___|
                                               
""""")
print ("Welcome UwU.Fucked Tool")
discordWebhook = input("Webhook: ")
discordcon = input("Content: ")
try:
    count = int(input("Number sends: "))
    if count < 0:
        raise ValueError("Error")
except ValueError as ve:
    print(f"Not Found! {ve}")
else:
    # 3. 指定回数だけ関数を実行する
    for _ in range(count):
        webhooksendevent()


