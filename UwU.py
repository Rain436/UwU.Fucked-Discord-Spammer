import time
import os

from discord_webhook import DiscordWebhook
from colorama import Fore, Back, Style, init

## Bad Code LOL

def webhooksendevent():
    webhook = DiscordWebhook(url=f"{discord_urlLibrary}", content=f"@here {discordcon} - UwU.Fucked", username="UwU.Fucked")
    time.sleep(0.3)
    response = webhook.execute()
os.system("title - UwU.Fucked - Webhook Fucker - & cls")
print(f""""{Fore.LIGHTMAGENTA_EX}                                   
 _____       _____   _____         _         _ 
|  |  |_ _ _|  |  | |   __|_ _ ___| |_ ___ _| |
|  |  | | | |  |  |_|   __| | |  _| '_| -_| . |
|_____|_____|_____|_|__|  |___|___|_,_|___|___|
                                               
""""")
print ("Welcome UwU.Fucked Tool")
discord_urlLibrary = input("Webhook: ")
discordcon = input("Content: ")
try:
    count = int(input("Number sends: "))
    if count < 0:
        raise ValueError("Error")
except ValueError as ve:
    print(f"Not Found! {ve}")
else:
    for _ in range(count):
        webhooksendevent()


