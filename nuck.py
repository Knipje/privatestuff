import discord

TOKEN = 'NTg2Mjk5MDY5OTM3NDgzNzk1.XPl_2Q.MLHMxqVm9MgiPh1uQwHFxkX5V2c'

GUILD = 281896256304054292

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return        
    
    if message.guild.id != 511082883570597920:
        return
    
    emote = discord.utils.get(message.guild.emojis,name="goldenspork")
    await message.add_reaction(emote)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')                        

client.run(TOKEN)