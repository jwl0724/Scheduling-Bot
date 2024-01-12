import asyncio
from discord.ext import tasks
import discord


async def start_timer(message, command):
    '''
    !timer #time (e.g., !timer 30) This will count down from 30 min. Default is 25 min
    Starts a timer counting down from 25 minutes
    given 25 minutes = 25*60 = 1500 seconds
    1500 seconds % 60 = 60 seconds
    '''
    # default timer is 25 min * 60 seconds = 1500 seconds
    default_timer_minutes = 25
    default_timer_seconds = default_timer_minutes * 60
    while default_timer_seconds != 0:
        default_timer_seconds -= 1
        await message.channel.send(f"Timer: {int(default_timer_seconds / 60)}: {default_timer_seconds % 60}")
        await asyncio.sleep(1)
    await message.channel.send(content="DONE")


async def process_timer_commands(message, command):
    match command:
        case 'timer':
            await start_timer(message, command)
        case 'restart':
            pass
        case 'pause':
            pass
        case 'stop':
            pass
