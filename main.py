import os
from keep_alive import keep_alive
import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix=["s!", "r!"],  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    activity=discord.Streaming(
        name="s!help or r!help", url="https://www.twitch.tv/ozziebeanie2"
    ),
  
)
bot.remove_command("help")
bot.author_id = 1006316083638190101  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
#    activity_string = 'on {} servers.'.format(len(bot.guilds))
#    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_string), status=discord.Status.do_not_disturb,)

#@bot.event
#async def on_message(message):
#  if bot.user.mentioned_in(message):
#    await message.channel.send(""""My prefixes are r! and s!
#    Do s!help or r!help to see what commands I got.
#    """)
#  await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send("That's not a real command!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send("You missed an argument!")
    elif isinstance(error, commands.MissingPermissions):
      await ctx.channel.send(f"You do not have the perms required!")
    # etc
    else:
        raise error

@bot.event
async def on_guild_join(guild):
    embed=discord.Embed(title="**Thank you for adding me!**", description=f"Thank you for adding me to {guild.name}!", color=0xe9fe81)
    embed.set_author(name=f"{guild.owner}", url="https://discord.gg/gjFmQnXy4B")
    embed.add_field(name="Prefixes", value="`s!` and `r!`", inline=True)
    await guild.text_channels[0].send(embed=embed)

extensions = [
    'cogs.basic_commands',
    'cogs.dev_commands',  # Same name as it would be if you were importing it
    'mod_cogs.main_mod',
    'cogs.help_command',
    'cogs.math_commands',
    'fun_cogs.game_commands',
    'fun_cogs.interaction_commands',
    'fun_cogs.funfacts'
]

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.

@bot.command()
async def verify(member):
    await member.add_roles(1049362070413516860)

#@bot.command()
#async def leaveg(ctx, *, guild_name):
#    if ctx.author == "1006316083638190101":
#      guild = discord.utils.get(bot.guilds, name=guild_name) # Get the guild by name
#      if guild is None:
#          print("No guild with that name found.") # No guild found
#          return
#      await guild.leave() # Guild found
#      await ctx.send(f"I left: {guild.name}!")
#    else:
#      await ctx.send("You're")

keep_alive()  # Starts a webserver to be pinged.
token = os.environ['token']
bot.run(token)  # Starts the bot