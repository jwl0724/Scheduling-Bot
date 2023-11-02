import discord
from checklist import *
from API_key import API_KEY
from responses import *

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

checklist_cmd = ['add', 'finish', 'remove', 'clear']
assignment_cmd = []
calendar_cmd = []
note_cmd = []
course_cmd = []

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

    # get message content, lower all letters, isolate the first string before white space
    command = message.content[1:].lower().split()[0]
    if command == 'help':
        await message.channel.send(help_response)
        return

    elif command in checklist_cmd:
        checklist_commands(message)

    else: 
        await message.channel.send('Type !help to see the available commands')
        return
    
    checklist_commands(message)
bot.run(API_KEY)