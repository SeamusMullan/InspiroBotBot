#Some Stupid thing by @seamo.m

import discord
import inspirobot
from requests.api import get
import Keys
import requests
import os

token = Keys.DISCORD_BOT_TOKEN #Discord Bot Token

client = discord.Client()



def getImage():



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('inspiro'):
        link = inspirobot.generate()
        r = requests.get(link)
        f = open('theInspire.jpg', 'wb').write(r.content)
        await message.channel.send(file=discord.file(f))
        os.remove(f)

client.run(token)