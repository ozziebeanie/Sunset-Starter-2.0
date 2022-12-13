import discord
from discord.ext import commands
import random 

class GameCommands(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
  
    @commands.command(aliases=['roll'])
    async def dice(self, ctx):
      roll = ['1','2','3','4','5','6']
      embed= discord.Embed(title="Coin Flip", color=0xc27c0e)
      embed.add_field(name="You rolled a:", value=random.choice(roll))
      await ctx.send(embed=embed)

    @commands.command(aliases=['coin', 'coinflip'])
    async def flip(self, ctx):
      coin = ['heads','tails']
      embed= discord.Embed(title="Coin flip", color=0xc27c0e)
      embed.add_field(name="You flipped a:", value=random.choice(coin))
      await ctx.send(embed=embed)

    @commands.command()
    async def eight_ball(self, ctx):
      possible_responses = ['That is a resounding no','It is not looking likely','Too hard to tell','It is quite possible','Definitely','Maybe so.']
      embed= discord.Embed(title="Magic 8Ball", color=0xc27c0e)
      embed.add_field(name="What'd you get?", value=random.choice(possible_responses))
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GameCommands(bot))