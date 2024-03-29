from API_key import DISCORD_API_KEY as API
from discord.ext import tasks
from datetime import datetime
import re
import discord
import checklist
import notes
import pomodoro
import courses
import assignments
import calendar_commands as cal
import static.responses as resp
import static.commands_list as cmd
import helpers as help


def main():
    intents = discord.Intents.default()
    intents.members, intents.message_content = True, True
    bot = discord.Client(intents=intents)
    command_prefix = '!'

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')

    @tasks.loop(hours=24)
    async def check_date():
        current_date = int(datetime.today().strftime('%d')) # returns current day
        if current_date == 20:
            reminder_channel = bot.get_channel(1193722212637736980)
            await reminder_channel.send('Reminder to renew U-Pass!')
            
    @bot.event
    async def on_message(message):
        # ignore messages without command prefix
        if not message.content or message.content[0] != command_prefix:
            return
        # ignore messages when only !
        if len(message.content) == 1:
            return
        if not re.search('^![a-zA-Z]', message.content):
            return 
        
        command = help.get_command(message.content)
        match command:
            case 'help':
                await message.channel.send(resp.help_response)

            case command if command in cmd.CHECKLIST_CMD:
                await checklist.process_checklist_commands(message, command)

            case command if command in cmd.ASSIGNMENT_CMD:
                await assignments.process_assignment_commands(message, command)

            case command if command in cmd.CALENDAR_CMD:
                await cal.process_calendar_commands(message, command)

            case command if command in cmd.NOTES_CMD:
                await notes.process_notes_commands(message, command)

            case command if command in cmd.COURSE_CMD:
                await courses.process_course_commands(message, command)

            case command if command in cmd.POMODORO_CMD:
                await pomodoro.start_timer(message, command)
            case _:
                await message.channel.send('Invalid command, type !help to see the available commands')

    bot.run(API)


if __name__ == '__main__':
    main()
    