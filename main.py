import discord
from API_key import API_KEY
from checklist import *
from static.responses import *
from checklist import *

intents = discord.Intents.default()
intents.members, intents.message_content = True, True

bot = discord.Client(intents=intents)

command_prefix = '!'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-----------')

@bot.event
async def on_message(message):
    # stop function if message isn't a command prompt or is from the bot itself
    if message.content[0] != command_prefix or message.author.id == bot.user.id: return
    command = message.content[1:].lower().split()[0]
    
    # process help command
    if command == 'help':
        await message.channel.send(help_response)
        return

    # process commands under checklist
    elif command in checklist_cmd:
        await checklist_commands(message)

    else: 
        await message.channel.send('Type !help to see the available commands')
        return
    
    checklist_commands(message)
bot.run(API_KEY)