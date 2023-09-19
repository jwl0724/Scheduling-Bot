import discord
import json

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)

command_prefix = '!'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-----------')

@bot.event
async def on_message(message):
    print(message)
    if message.content[0] == '!':
        await message.channel.send('it works')


bot.run('MTE1MzUyNTMzNzY5OTkwOTY5Mg.GoyC-R.FShuoH5MVELSucNfuZ4i9bLo3tt_9P3DqmcT7A')