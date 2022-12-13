import discord
from discord.ext import commands
import random

class BasicCommands(commands.Cog, name='Basic Commands'):
    '''These are basic commands anyone can use'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, message=None):
        '''
        Makes the bot say something.
        '''
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(description="Bots latency.")
    async def ping(self, ctx):
        '''
        Sends how fast the bot is running.
        '''
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! My latency is {latency}ms.")

    @commands.command()
    async def servers(self, ctx):
        '''
        Shows how many servers the bot has joined.
        '''
        servers = list(self.bot.guilds)
        await ctx.send(f"I have joined over {str(len(servers))} guilds.")

#    @commands.command()
#    async def support(self, ctx):
#      await ctx.send("https://discord.gg/gjFmQnXy4B")

    @commands.command()
    async def invite(self, ctx):
      await ctx.send("https://discord.com/api/oauth2/authorize?client_id=1046832615975550976&permissions=1614940597574&scope=bot")
      await ctx.send("Thanks for inviting me!")

    @commands.command()
    async def support(self, ctx):
      embed=discord.Embed(title="Support server", description="Thank you for deciding to join!", color=0xe91e63)
      embed.set_image(url='https://media.giphy.com/media/yC5LBDWXxaMmI7cIjN/giphy.gif')
      embed.add_field(name="Server", value="https://discord.gg/gjFmQnXy4B",inline=True)
      await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(BasicCommands(bot))
