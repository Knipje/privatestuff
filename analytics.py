import discord
import asyncio
import json
import os
import datetime

TOKEN = 'NTc4MzAzODEyODY4MjQzNDU2.XNxpdg.UO3VapBgEsIcu7gUrkpguknLCXY'

GUILD = 146404426746167296

client = discord.Client()

path = os.path.dirname(os.path.abspath(__file__)) + "/raw_data.json"

with open(path,'w') as outfile:
    outfile.write('[]')

def checkDiscordRoles(message):
    roles = message.author.roles
    for role in roles:
        if role.name in ['Mods', 'the mad botter']:
            return True
    return False

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
        
    if message.content.startswith('!analyticslist'):
        if checkDiscordRoles(message):
            filesend = discord.File(path, spoiler=False)
            await message.channel.send(file=filesend)
            with open(path,'w') as outfile:
                outfile.write('[]')
        return

    if message.guild.id != GUILD:
        return 


    data = json.loads(open(path).read())
    now = message.created_at
    out = {'datetime':str(now), 'channel': str(message.channel.name), 'author': str(message.author.name)}

    data.append(out)

    with open(path,'w') as outfile:
        json.dump(data,outfile)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
