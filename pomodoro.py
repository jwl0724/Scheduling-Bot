from discord.ext import tasks
import discord


@tasks.loop()
def start_timer(message, command):
    pass

async def process_timer_commands(message, command):
    match command:
        case 'timer':
            stop_watch = Timer(10, await stop_timer(message))
            stop_watch.start()
        case 'restart':
            pass
        case 'pause':
            pass
        case 'stop':
            pass