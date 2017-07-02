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
    memberjoined = ('User: ') + str(member) + ('\nActn: Joined server\n') + ('Date: {:%d %b %Y}\n').format(datetime.datetime.now()) + ('-----------------------------------------------------------\n')
    f.write(memberjoined)
    f.close()
    print(memberjoined)
	
@client.event
async def on_member_remove(member):
    server = member.server
    fmt = 'The user {0.mention} has left the server!'
    await client.send_message(server, fmt.format(member, server))
    f = open('log.txt', 'a')
    memberleave = ('User: ') + str(member) + ('\nActn: Left server\n') + ('Date: {:%d %b %Y}\n').format(datetime.datetime.now()) + ('-----------------------------------------------------------\n')
    f.write(memberleave)
    f.close()
    print(memberleave)

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$date'):
        msg = 'The current date is {:%d %b %Y} in Australia'.format(datetime.datetime.now())
        await client.send_message(message.channel, msg)	

    if message.content.startswith('intro'):
        msg = 'Hello {0.author.mention} I am raxbot! Nice to meet you :D'.format(message)
        await client.send_message(message.channel, msg)	
	
@client.event
async def delete_messages(messages):
	if message.content.startswith('$clear'):
		async for msg in client.logs_from(message.channel, limit=100):
			await client.delete_messages(messages)		

client.run('CLIENT TOKEN HERE')
