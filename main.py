import discord
import requests
import os
import time
from datetime import datetime

import yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

webhook_url = config['webhook_url']

def filter_detected():
    json = {"content":None,"embeds":[{"title":"AutoFilter","description":"```A new filter has been detected!```",
            "color":7132927,"footer":{"text":"AutoFilter v1.0"},"timestamp":str(datetime.now().isoformat())}],"attachments":[]}
    
    requests.post(webhook_url, json=json)

def applying_filter():
    json = {"content":None,"embeds":[{"title":"AutoFilter","description":"```Applying new filter...```",
            "color":16579653,"footer":{"text":"AutoFilter v1.0"},"timestamp":str(datetime.now().isoformat())}],"attachments":[]}
    
    requests.post(webhook_url, json=json)

def applied_filter():
    json = {"content":None,"embeds":[{"title":"AutoFilter","description":"```Successfully applied new filter, restarting the bot now...```",
            "color":7470149,"footer":{"text":"AutoFilter v1.0"},"timestamp":str(datetime.now().isoformat())}],"attachments":[]}
    
    requests.post(webhook_url, json=json)

def success():
    json = {"content":None,"embeds":[{"title":"AutoFilter","description":"```All actions completed successfully, the bot is now running!```",
            "color":7470149,"footer":{"text":"AutoFilter v1.0"},"timestamp":str(datetime.now().isoformat())}],"attachments":[]}
    
    requests.post(webhook_url, json=json)

server_channel_id = config['server_channel_id']
token = config['token']


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {str(client)}")


@client.event
async def on_message(message):
    channel_id = message.channel.id
    if channel_id == server_channel_id:
        try:
            attachment_url = message.attachments[0].url
            os.system("tmux kill-session -t bin")
            print("Killed session")
            applying_filter()
            with open("filter.json", "w+") as f:
                print("Wrote filter")
                try:
                    r = requests.get(attachment_url).text
                    f.write(r)
                except Exception as e:
                    print("error", e)
                    return ""
                applied_filter()
            time.sleep(5)
            os.system("tmux new-session -d -s bin './binmaster-v2-linux'")
            print("Started session")
            success()
        except:
            print("No attachment found")


client.run(token)