#Some Stupid thing by @seamo.m

import discord
import inspirobot
from requests.api import get
import requests
import os
from time import sleep

# This file has not been uploaded to GitHub. To implement a custom key, create a Keys.py file and create a string called DISCORD_BOT_TOKEN
import Keys
token = Keys.DISCORD_BOT_TOKEN

client = discord.Client()

def Generate():
    link = inspirobot.generate()
    r = requests.get(link)
    open('theInspire.jpg', 'wb').write(r.content)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('inspiro'):
        Generate()
        await message.channel.send(file=discord.File("theInspire.jpg"))
        if os.path.exists("theInspire.jpg"):
            os.remove("theInspire.jpg")

client.run(token)
