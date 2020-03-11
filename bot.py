import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')



client.run('Njg3MDk1Nzc4OTA0Mzc1MzA5.Xmg80Q.slrKk5sIGtkkAld_tqkFWAMhd6s')
