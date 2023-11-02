import discord
from API_key import API_KEY
from checklist import *
from static.responses import *
from checklist import *
from static.commands_list import *

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

    # get inputted command
    command = message.content[1:].lower().split()[0]
    
    match command:
        case 'help':
            await message.channel.send(help_response)

        case command if command in CHECKLIST_CMD:
            checklist_commands(message, command)

        case command if command in ASSIGNMENT_CMD:
            pass

        case command if command in CALENDER_CMD:
            pass

        case command if command in NOTE_CMD:
            pass

        case command if command in COURSE_CMD:
            pass

        case _:
            await message.channel.send('Type !help to see the available commands')
            return

bot.run(API_KEY)