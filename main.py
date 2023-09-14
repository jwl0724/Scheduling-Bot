import discord
import json

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)

command_prefix = '&&'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-----------')

bot.run('MTA3MjAxOTQwMDMxNzczMDkxNw.G5g0No.a4tRzOb5NoMVMgKhcwgrSYXEFt6MnVhOCX1wQc')