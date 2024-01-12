import asyncio
import re

from discord.ext import tasks
import discord

DEFAULT_TIMER_MINUTES = 25
is_timer_paused = False
paused_timer_seconds = 0


async def start_timer(message, command):
    '''
    !timer #time (e.g., !timer 30) This will count down from 30 min. Default is 25 min
    Starts a timer counting down from 25 minutes
    given 25 minutes = 25*60 = 1500 seconds
    1500 seconds % 60 = 60 seconds
    '''
    # default timer is 25 min * 60 seconds = 1500 seconds
    global is_timer_paused, paused_timer_seconds
    default_timer_seconds = DEFAULT_TIMER_MINUTES * 60
    while default_timer_seconds != 0:
        await message.channel.send(f"Timer: {default_timer_seconds // 60}: {default_timer_seconds % 60:02d}")
        await asyncio.sleep(1)
        default_timer_seconds -= 1
        if is_timer_paused:
            paused_timer_seconds = default_timer_seconds
            await asyncio.sleep(1)
    await message.channel.send(content="DONE")


def restart_timer():
    return DEFAULT_TIMER_MINUTES

def pause_timer():
    global is_timer_paused
    is_timer_paused = True

def resume_timer():
    global is_timer_paused
    is_timer_paused = False


async def process_timer_commands(message, command):
    match command:
        case 'timer':
            await start_timer(message, command)
        case 'restart':
            await message.channel.send(f"Timer Restarted @ {DEFAULT_TIMER_MINUTES} minutes ")
            await start_timer(message, command)

        case 'pause':
            pause_timer()
            await message.channel.send(f"Timer paused @ {paused_timer_seconds // 60}:{paused_timer_seconds % 60:02d}")

        case 'resume':
            resume_timer()
            await message.channel.send(f"Timer resumed@ {paused_timer_seconds // 60}:{paused_timer_seconds % 60:02d}")

        case 'stop':
            pass
