import discord
import asyncio
import datetime
import os

from discord.ext import commands

description = 'Custom rax bot'
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
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    f = open('log.txt', 'a')
    memberjoined = str(member) + (' has joined the server @ {:%b %d %Y}\n').format(datetime.datetime.now())
    f.write(memberjoined)
    f.close()
    print(memberjoined)
	
@client.event
async def on_member_remove(member):
    server = member.server
    f = open('log.txt', 'a')
    memberleave = str(member) + (' has left the server @ {:%b %d %Y}\n').format(datetime.datetime.now())
    f.write(memberleave)
    f.close()
    print(memberleave)
	
@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$date'):
        msg = 'Todays date is {:%b %d %Y} in Australia'.format(datetime.datetime.now())
        await client.send_message(message.channel, msg)	

		
client.run('CLIENT_TOKEN_HERE')
