import discord
from discord.ext import commands
from datetime import timedelta

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)

        embed = discord.Embed(title=f"{ctx.author.name} kicked: {member.name}", description=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(user=member, reason=reason)

        embed = discord.Embed(title=f"{ctx.author.name} banned: {member.name}", description=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)

        embed = discord.Embed(title=f"{ctx.author.name} unbanned: {member.name}", description=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount+1)

        embed = discord.Embed(title=f"{ctx.author.name} purged: {ctx.channel.name}", description=f"{amount} messages were cleared")
        await ctx.send(embed=embed)

#    @commands.command()
#    @commands.guild_only()
#    @commands.has_guild_permissions(mute_members=True)
#    async def timeout(self, ctx, member, minutes, reason=None):
#      duration = timedelta(minutes=minutes)
#      await member.timeout(duration, reason=reason)
#      await ctx.send(f'{member.mention} was timeouted until for {duration}')

def setup(bot):
    bot.add_cog(Moderation(bot))