#
#  GD-Connect bot server
#
# Requires ".envDiscord" and ".envGuilded" files in the
# same directory as "main.py"
#
# Example .env files
#
# .env
#GUILDED_TOKEN=guildedtoken

# and

# .env
#DISCORD_TOKEN=discordtoken

# setup
# $ pip install python-dotenv
# $ pip install asyncio
# $ python3 main.py


import os

import discord
import guilded
from dotenv import load_dotenv
import asyncio

load_dotenv(".envDiscord")
load_dotenv(".envGuilded")
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILDED_TOKEN = os.getenv('GUILDED_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

clientDiscord = discord.Client(intents=intents)
clientGuilded = guilded.Client()

guildedChannel = "be2cf7d2-a635-41e6-898c-9253c0a4b0fa"
discordChannel = 1228801393847177317

async def send(message, platform):
    if platform == "d":
        channelDiscord = clientDiscord.get_channel(discordChannel)
        await channelDiscord.send(message)
    elif platform == "g":
        channelGuilded = await clientGuilded.fetch_channel(guildedChannel)
        await channelGuilded.send(message)

# Discord segment

@clientDiscord.event
async def on_ready():
    print(f'{clientDiscord.user} has connected to Discord!')
    await send("GDConnect started", "d")

@clientDiscord.event
async def on_message(message):
    if message.author == clientDiscord.user:
            return
    if message.channel.id == discordChannel:
        await send(message.author.global_name + ": " + message.content, "g")

# Guilded segment

@clientGuilded.event
async def on_ready():
    print(f'{clientGuilded.user} has connected to Guilded!')
    await send("GDConnect started", "g")

@clientGuilded.event
async def on_message(message):
    if message.author.name == "GDConnect":
        return
    if message.channel.id == guildedChannel:
        await send(message.author.name + ": " + message.content, "d")

async def run_bots():
    discord_task = clientDiscord.start(DISCORD_TOKEN)
    guilded_task = clientGuilded.start(GUILDED_TOKEN)
    
    await asyncio.gather(discord_task, guilded_task)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run_bots())
    except KeyboardInterrupt:
        loop.run_until_complete(clientDiscord.close())
        loop.run_until_complete(clientGuilded.close())
