import discord
from checklist import *
from API_key import API_KEY

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
    if message.content[0] != command_prefix or message.author.id == bot.user.id:
        return

    # get message content, lower all letters, isolate the first string before white space
    command = message.content[1:].lower().split()[0]
    if command == 'help':
        await message.channel.send('''
                                   CALENDAR COMMANDS
!calendar - see visual calendar

ASSIGNMENTS COMMAND
!save month/day 'assignment' (ex. !save 09/27 'midterm')
!assignments - display lists of assignments due 
!delete 'assignment' - remove assignment from calendar

CHECKLIST COMMANDS
!add 'task' - add tasks to a checklist  (ex. !add 'Do math homework')
!finish #entry - crosses off checklist (ex. !finish #3)
!remove #entry - remove entry from checklist
!clear - remove all entries from checklist
                                   
NOTE COMMANDS
!note 'notes' - save notes to storage (ex. !note 'this is an example')                       
!erase #entry - remove the note at the entry number
!wipe - erase all notes
!edit - #entry - edit the note at the entry number
                                   
COURSE MANAGEMENT COMMANDS
!courses - list courses for the week
!add_course 'course' - add course to list (ex. !add_course 'COMP 1510')
!remove_course 'course' - remove course from list
!wipe_courses - remove all courses from list
!edit_course 'course' - edit details of the course
!next - Show next course on schedule and how much time until then
                                ''')
        return

    elif command in checklist_cmd:
        checklist_commands(message)

    else: 
        await message.channel.send('Type !help to see the available commands')
        return
    
    checklist_commands(message)
bot.run(API_KEY)