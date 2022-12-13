import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    embed = discord.Embed(title="Help", description="Use r!help or s!help <command> or <cog> for extended information on the command or cog (Don't add commands to the cog)", color=0x3498db)
    embed.add_field(name="Moderation Commands", value = "Kick, Ban, Unban, Purge")
    embed.add_field(name="Interaction Commands", value="Hug, Middle, Wave, Kill, Kiss, Slap, Carry, Sunset, Grass, FunFact")
    embed.add_field(name="Basic Commands", value="Say, Ping, Servers, Support, Invite")
    embed.add_field(name="Game Commands", value="Dice, Flip, Eight_Ball")
    embed.add_field(name="Math Commands", value="Add, Sub, Div, Multi")
    await ctx.send(embed=embed)

  @help.command()
  async def moderation(self, ctx):
    embed=discord.Embed(title="Help", description="Moderation Commands", color=0x99aab5)
    embed.add_field(name="Kick", value="Kicks a member from the guild.", inline=True)
    embed.add_field(name="Ban", value="Bans a member from the guild.", inline=True)
    embed.add_field(name="Unbans", value="Unbans a member from the guild.", inline=True)
    embed.add_field(name="Purge", value="Purgaes a number of messages from a channel. Default is set to 15 messages.")
    await ctx.send(embed=embed)

  @help.command()
  async def interaction(self, ctx):
    embed=discord.Embed(title="Help", description="Interaction Commands", color=0xe67e22)
    embed.add_field(name="Hug", value="Hugs a member.", inline=True)
    embed.add_field(name="Middle", value="Sticks your middle finger at a member.", inline=True)
    embed.add_field(name="Wave", value="Waves at a member.", inline=True)
    embed.add_field(name="Kill", value="Kills a member.", inline=True)
    embed.add_field(name="Kiss", value="Kisses a member.", inline=True)
    embed.add_field(name="Slap", value="Slaps a member.", inline=True)
    embed.add_field(name="Carry", value="Carries a member.", inline=True)
    embed.add_field(name="Sunset", value="Look at the sunset!", inline=True)
    embed.add_field(name="Grass", value="Go touch some grass!", inline=True)
    embed.add_field(name="FunFact", value="Sends a fun fact!", inline=True)
    await ctx.send(embed=embed)

  @help.command()
  async def basic(self, ctx):
    embed=discord.Embed(title="Help", description="Basic Commands", color=0xe91e63)
    embed.add_field(name="Say", value="Says something as the bot", inline=True)
    embed.add_field(name="Ping", value="Pong!", inline=True)
    embed.add_field(name="Servers", value="Shows how many guilds the server is in.", inline=True)
    embed.add_field(name="Support", value="Sends a invite link to the support server.", inline=True)
    embed.add_field(name="Invite", value="Sends a invite link for the bot.", inline=True)
    await ctx.send(embed=embed)

  @help.command()
  async def math(self, ctx):
    embed=discord.Embed(title="Help", description="Math Commands")
    embed.add_field(name="Add", value="Adds two numbers together", inline=True)
    embed.add_field(name="Sub", value="Subtracts two numbers together", inline=True)
    embed.add_field(name="Div", value="Divides two numbers together", inline=True)
    embed.add_field(name="Multi", value="Mutliplys two numbers together", inline=True)
    await ctx.send(embed=embed)
  
  @help.command()
  async def game(self, ctx):
    embed=discord.Embed(title="Help", description="Game Commands", color=0xc27c0e)
    embed.add_field(name="Dice", value="Rolls a dice.", inline=True)
    embed.add_field(name="Flip", value="Flips a coin", inline=True)
    embed.add_field(name="Eight_Ball", value="Shakes a Magic 8 Ball", inline=True)
    await ctx.send(embed=embed)

  
  @help.command()
  async def kick(self, ctx):
    embed = discord.Embed(title="Kick", description="Kicks a member from the guild", color=0x99aab5)
    embed.add_field(name="**Syntax**", value=f"r!kick or s!kick <member> [reason]")
    await ctx.send(embed=embed)

  @help.command()
  async def ban(self, ctx):
    embed = discord.Embed(title="Ban", description="Bans a member from the guild", color=0x99aab5)
    embed.add_field(name="**Syntax**", value="r!ban or s!ban <member> [reason]")
    await ctx.send(embed=embed)

  @help.command()
  async def unban(self, ctx):
    embed = discord.Embed(title="Unban", description="Unbans a member from the guild", color=0x99aab5)
    embed.add_field(name="**Syntax**", value="r!unban or s!unban <member> [reason]")
    await ctx.send(embed=embed)

  @help.command()
  async def purge(self, ctx):
    embed = discord.Embed(title="Purge", description="Purges a number of message from a channel. Default is 15 message", color=0x99aab5)
    embed.add_field(name="**Syntax**", value="r!purge or s!purge [messages]")
    await ctx.send(embed=embed)

  @help.command()
  async def hug(self, ctx):
    embed = discord.Embed(title="Hug", description="Hugs a User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!hug or s!hug <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def middle(self, ctx):
    embed = discord.Embed(title="Middle", description="Sticks Middle Finger at User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!middle or s!middle <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def wave(self, ctx):
    embed = discord.Embed(title="Wave", description="Waves at User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!wave or s!wave <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def kill(self, ctx):
    embed = discord.Embed(title="Kill", description="Kills a User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!kill or s!kill <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def kiss(self, ctx):
    embed = discord.Embed(title="Kiss", description="Kisses a User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!kiss or s!kiss <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def slap(self, ctx):
    embed = discord.Embed(title="Slap", description="Slaps a User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!slap or s!slap <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def carry(self, ctx):
    embed = discord.Embed(title="Carry", description="Carries a User", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!carry or s!carry <member>")
    await ctx.send(embed=embed)

  @help.command()
  async def sunset(self, ctx):
    embed= discord.Embed(title="Sunset", description="Look at the sunset!", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!sunset or s!sunset", inline=True)
    await ctx.send(embed=embed)

  @help.command()
  async def grass(self, ctx):
    embed= discord.Embed(title="Grass", description="Go touch some grass!", color=0xe67e22)
    embed.add_field(name="**Syntax**", value="r!grass or s!grass", inline=True)
    await ctx.send(embed=embed)

  @help.command()
  async def funfact(self, ctx):
    embed= discord.Embed(title="FunFact", description="Sends a fun fact!")
    embed.add_field(name="**Syntax**", value="r!funfact or s!funfact", inline=True)
    embed.add_field(name="**Aliases**", value="Funfact and Funfacts")
    await ctx.send(embed=embed)
    
  @help.command()
  async def say(self, ctx):
    embed = discord.Embed(title="Say", description="Make the bot say something", color=0xe91e63)
    embed.add_field(name="**Syntax**", value="""r!say or s!say "<message>" """)
    embed.add_field(name="Warning", value="You need to add quotes in your message in order to have a multiword quote to be said.")
    await ctx.send(embed=embed)

  @help.command()
  async def ping(self, ctx):
    embed = discord.Embed(title="Ping", description="Pong!", color=0xe91e63)
    embed.add_field(name="**Syntax**", value="r!ping or s!ping")
    await ctx.send(embed=embed)

  @help.command()
  async def servers(self, ctx):
    embed = discord.Embed(title="Servers", description="Sends how many guilds the bot has joined!", color=0xe91e63)
    embed.add_field(name="**Syntax**", value="r!servers or s!servers")
    await ctx.send(embed=embed)

  @help.command()
  async def support(self, ctx):
    embed = discord.Embed(title="Support", description="Sends a invite link to the support server!", color=0xe91e63)
    embed.add_field(name="**Syntax**", value="r!support or s!support")
    await ctx.send(embed=embed)

  @help.command()
  async def invite(self, ctx):
    embed = discord.Embed(title="Invite", description="Sends a invite link for the bot!", color=0xe91e63)
    embed.add_field(name="**Syntax**", value="r!invite or s!invite")
    await ctx.send(embed=embed)

  @help.command()
  async def dice(self, ctx):
    embed = discord.Embed(title="Diceroll", description="Rolls a dice", color=0xc27c0e)
    embed.add_field(name="**Syntax**", value="r!dice or s!dice")
    embed.add_field(name="**Aliases**", value="Roll and Dice")
    await ctx.send(embed=embed)

  @help.command()
  async def flip(self, ctx):
    embed = discord.Embed(title="Flip Coin", description="Flips a coin", color=0xc27c0e)
    embed.add_field(name="**Syntax**", value="r!flip or s!flip")
    embed.add_field(name="**Aliases**", value="Flip, Coin, and CoinFlip")
    await ctx.send(embed=embed)

  @help.command()
  async def eight_ball(self, ctx):
    embed = discord.Embed(title="Eight_Ball", description="Shakes a Magic 8 Ball", color=0xc27c0e)
    embed.add_field(name="**Syntax**", value="r!eight_ball or s!eight_ball")
    await ctx.send(embed=embed)

  @help.command()
  async def add(self, ctx):
    embed = discord.Embed(title="Add", description="Adds two numbers together")
    embed.add_field(name="**Syntax**", value="r!add or s!add <number 1> <number 2>")
    await ctx.send(embed=embed)

  @help.command()
  async def sub(self, ctx):
    embed = discord.Embed(title="Sub", description="Subtracts two numbers together")
    embed.add_field(name="**Syntax**", value="r!sub or s!sub <number 1> <number 2>")
    await ctx.send(embed=embed)

  @help.command()
  async def div(self, ctx):
    embed = discord.Embed(title="Div", description="Divides two numbers together")
    embed.add_field(name="**Syntax**", value="r!div or s!div <number 1> <number 2>")
    await ctx.send(embed=embed)

  @help.command()
  async def multi(self, ctx):
    embed = discord.Embed(title="Multi", description="Multiplys two numbers together")
    embed.add_field(name="**Syntax**", value="r!multi or s!multi <number 1> <number 2>")
    await ctx.send(embed=embed)
  
def setup(bot):
  bot.add_cog(HelpCommand(bot))