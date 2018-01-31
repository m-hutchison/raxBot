import discord
import asyncio
import datetime
import os
import sys
import random
import imp

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
		
    if message.content.startswith('$killbot'):
        msg = 'Terminating my session, goodbye.'.format(message)
        await client.send_message(message.channel, msg)	
        quit()
        pass

    if message.content.startswith('$memes'):
        channel = client.get_channel("302251062134439936")
        memePath = r'INSERT MEME DIRECTORY'
        randMeme = os.path.join(memePath, random.choice(os.listdir(memePath))) 
        await client.send_file(channel, randMeme, content='Incoming dank meme:')

    if message.content.startswith('$reload'):
        msg = 'Restarting my session.. beep boop.'.format(message)
        await client.send_message(message.channel, msg)	
        pass
        quit()

@client.event
async def delete_messages(messages):
    if message.content.startswith('$clear'):
        async for msg in client.logs_from(message.channel, limit=100):
            await message.delete(messages)

client.run('INSERT TOKEN HERE')
