import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('Njg3MDk1Nzc4OTA0Mzc1MzA5.Xmgx3w.vQgtpDBP4ZUBJo2LW0AQsmvSF6Q')
