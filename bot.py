import discord
from discord.ext import commands

import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')

#@client.event
#async def on_member_join(member):
#    print(f'{member} has joined a server.')


#@client.event
#async def on_member_remove(member):
#    print(f'{member} has left a server.')



client.run('Njg3MDk1Nzc4OTA0Mzc1MzA5.Xmg80Q.slrKk5sIGtkkAld_tqkFWAMhd6s')
