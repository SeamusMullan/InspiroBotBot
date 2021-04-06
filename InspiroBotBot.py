#Some Stupid thing by @seamo.m

import discord
import inspirobot
import Keys

token = Keys.DISCORD_BOT_TOKEN #Discord Bot Token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Discord Quality Of Life Stuff

    if message.content.startswith('inspiro'):
        await message.channel.send(embed = inspirobot.generate())

client.run(token)