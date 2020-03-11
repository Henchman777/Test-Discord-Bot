import discord
from discord.ext import commands, tasks
from itertools import cycle

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    #@commands.Cog.listener()
    #async def on_ready(self):
        #change_status.start()
        #await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Eating Lunch'))
        #print('Bot is ready.')

    # Commands
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ping(self, ctx):
        await ctx.send('Pong!')


#status = cycle(['Status 1', 'Status 2'])
#@tasks.loop(seconds=10)
#async def change_status():
#    await client.change_presence(activity=discord.Game(next(status)))


def setup(client):
    client.add_cog(Example(client))
