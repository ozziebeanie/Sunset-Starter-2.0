import discord
from discord.ext import commands
import random

class InteractionCommands(commands.Cog):
    '''
    Contains fun commands, activities and more!
    '''
    def __init__(self, bot,):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        '''
        Hugs the chosen person.
        '''
        hug_gifs = [
          'https://media.tenor.com/eoZ25OAvxkIAAAAd/chobits-hideki-motosuwa.gif',
          'https://cdn.weeb.sh/images/jJv2H5adf.gif',
          'https://media.tenor.com/J7eGDvGeP9IAAAAC/enage-kiss-anime-hug.gif',
          'https://media.tenor.com/kCZjTqCKiggAAAAC/hug.gif',
          'https://media.tenor.com/RWD2XL_CxdcAAAAd/hug.gif'
        ]
        gif = random.randrange(0,5)
        embed = discord.Embed(title=f"```{ctx.author.name}``` hugged ```{member.name}```", color=0xe67e22)
        embed.set_image(url=f'{hug_gifs[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def middle(self, ctx, member: discord.Member):
        '''
        Sticks up the middle finger to the chosen person.
        '''
        middle_gifs = [
          'https://c.tenor.com/szJmB0ISf7UAAAAM/anime-girl.gif',
          'https://media.tenor.com/eSiR-TcUZqgAAAAS/oniai-anastasia-nasuhara.gif',
          'https://media.tenor.com/ygNrDasDYYYAAAAC/attackontitan-shingekinokyojin.gif',
          'https://media.tenor.com/0CrbRX_WsMkAAAAC/anime-animu.gif',
          'https://media.tenor.com/BJHzwmUeXVwAAAAC/fuck-u.gif'
        ]
        gif = random.randrange(0,5)
        embed = discord.Embed(title=f"{ctx.author.name} Stuck Up Middle Finger At {member.name}", color=0xe67e22)
        embed.set_image(url=f'{middle_gifs[gif]}')
        await ctx.send(embed=embed)


    @commands.command()
    async def wave(self, ctx, member: discord.Member):
        '''
        Waves at the chosen person.
        '''
        gif = random.randrange(0,5)
        wave_gifs = [
          'https://c.tenor.com/uGN3n2O03GIAAAAC/anime-wave.gif',
          'https://media.tenor.com/qlT4AO1LID0AAAAC/anime-wave.gif',
          'https://media.tenor.com/NjsosaK61UIAAAAC/anime-girl.gif',
          'https://media.tenor.com/AuBOgaPV41cAAAAC/shinya-shinyahiragi.gif',
          'https://media.tenor.com/meiDmToBf4sAAAAC/anime-wave.gif'
        ]
        embed = discord.Embed(title=f"{ctx.author.name} waved at {member.name}", color=0xe67e22)
        embed.set_image(url=f'{wave_gifs[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member):
        '''
        Kills the chosen person.
        '''
        gif = random.randrange(0,5)
        kill_gifs = [
          'https://cdn.weeb.sh/images/HyXTiyKw-.gif',
          'https://media.tenor.com/Ze50E1rW44UAAAAS/akudama-drive.gif',
          'https://media.tenor.com/G4SGjQE8wCEAAAAC/mikey-tokyo.gif',
          'https://media.tenor.com/xQ9HqX1H9tsAAAAd/anime-dies-i-hate-you.gif',
          'https://media.tenor.com/NbBCakbfZnkAAAAC/die-kill.gif'
        ]
        embed = discord.Embed(title=f"{ctx.author.name} has killed {member.name}", color=0xe67e22)
        embed.set_image(url=f'{kill_gifs[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        '''
        Kisses the chosen person.
        '''
        gif = random.randrange(0,5)
        kiss_gifs = [
          'https://cdn.weeb.sh/images/BJSdQRtFZ.gif',
          'https://media.tenor.com/YHxJ9NvLYKsAAAAC/anime-kiss.gif',
          'https://media.tenor.com/06lz817csVgAAAAd/anime-anime-kiss.gif',
          'https://media.tenor.com/jnndDmOm5wMAAAAC/kiss.gif',
          'https://media.tenor.com/dn_KuOESmUYAAAAC/engage-kiss-anime-kiss.gif'
        ]
        embed = discord.Embed(title=f"{ctx.author.name} kissed {member.name}", color=0xe67e22)
        embed.set_image(url=f'{kiss_gifs[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        '''
        Slaps the chosen person.
        '''
        gif = random.randrange(0,5)
        slap_gifs = [
          'https://cdn.weeb.sh/images/SJdXoVguf.gif',
          'https://media.tenor.com/oYsWol5_exYAAAAC/slap.gif',
          'https://media.tenor.com/sDF-c_-qKnEAAAAC/anime.gif',
          'https://media.tenor.com/XiYuU9h44-AAAAAC/anime-slap-mad.gif',
          'https://media.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif'
        ]
        embed = discord.Embed(title=f"{ctx.author.name} slapped {member.name}", color=0xe67e22)
        embed.set_image(url=f'{slap_gifs[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def carry(self, ctx, member: discord.Member):
        '''
        Carries the chosen person.
        '''
        gif = random.randrange(0,5)
        carry_gifs = [
          'https://media.tenor.com/QPb9KhjDIW0AAAAC/carry.gif',
          'https://media.tenor.com/pFl76pkB7ZIAAAAC/tanaka-carry.gif',
          'https://media.tenor.com/qN6duKyjzaYAAAAC/bakemonogatari-carry.gif',
          'https://media.tenor.com/fg5LkU4gnacAAAAC/anime-anime-carry.gif',
          'https://media.tenor.com/W4Voi07VHcsAAAAC/anime-josee.gif'
        ]
        embed = discord.Embed(title=f"{ctx.author.name} is carrying {member.name}. Looks Like They Want Down", color=0xe67e22)
        embed.set_image(url=f'{carry_gifs[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def sunset(self, ctx):
        gif = random.randrange(0,5)
        sunsets = [
          'https://media.tenor.com/ddzDqS20za0AAAAC/sunset-shimmer-sunsets.gif',
          'https://media.tenor.com/40sGw_opXwIAAAAC/redsky-ocean.gif',
          'https://media.tenor.com/qf_NWisSFZQAAAAd/sunset-ocean.gif',
          'https://media.tenor.com/-RNOB5xDZ5gAAAAC/sunset.gif',
          'https://media.tenor.com/d4HTrN_bbuQAAAAC/sunset-tropical-island.gif'
        ]
        embed=discord.Embed(title="Look at the sunset!", color=0xe67e22)
        embed.set_image(url=f'{sunsets[gif]}')
        await ctx.send(embed=embed)

    @commands.command()
    async def grass(self, ctx):
        gif = random.randrange(0,2)
        grass = [
          'https://media.tenor.com/4yx6wK51ezsAAAAd/nathan-touch-some-grass.gif',
          'https://media.tenor.com/nhPRQbvPSB4AAAAd/touch-grass.gif'
        ]
        embed=discord.Embed(title="Go touch some grass!", color=0xe67e22)
        embed.set_image(url=f'{grass[gif]}')
        await ctx.send(embed=embed)
  
def setup(bot):
    bot.add_cog(InteractionCommands(bot))