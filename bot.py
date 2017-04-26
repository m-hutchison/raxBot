import discord
import asyncio
import datetime

from discord.ext import commands

description = 'Custom bot'
bot_prefix = '$'

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client)

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$date'):
        msg = 'Todays date is {:%b, %d %Y} in Australia'.format(datetime.datetime.now())
        await client.send_message(message.channel, msg)    

        
client.run('INSERT_UR_DISCORD_TOKEN_HERE_PLS')
