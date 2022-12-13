import discord
from discord.ext import commands 
import random

class FunFacts(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(aliases=['funfacts'])
  async def funfact(self, ctx):
    funfacts = [
      'A cat was the Mayor of an Alaskan town for 20 years',
      'Rhubarb grows so fast, you can hear it',
      'Because the sun is low on the horizon, sunlight passes through more air at sunset and sunrise than during the day, when the sun is higher in the sky',
      'Sunsets on Mars appears blue',
      'A popular tradition in Japan is to eat KFC for Christmas. It is so popular, in fact, that orders must be placed two months in advance.',
      'Napoleon Was Once Attacked By a Horde of Bunnies.',
      'Bananas are radioactive.',
      '"Girls Just Wanna Have Fun" is a cover by some dude. The original is by a guy named Robert Hazard.',
      'Taylor Swift has a framed picture of Kanye West interrupting her at the 2009 MTV Video Music Awards in her living room. Its captioned, "Life is full of little interruptions."',
      'There are nearly 3.5 billion active social media users, and every 6.4 seconds a new account has been created',
      'From 1937 To 1953, NBCs Today Show Had A Chimpanzee Co-Host Named J. Fred Muggs. It Is Estimated He Brought In The Network Around $100 Million.',
      'The Vatican Had Music Which Was Forbidden To Be Copied And Was Only Played Twice Per Year. It Was Secret For Almost 150 Years Until A 14-Year-Old Mozart Heard It And Transcribed It From Memory.',
      'There Is A Liquid That You Can Breathe In Called Perfluorohexane. Animals Can Be Submerged In A Bath Of Perfluorohexane Without Drowning.',
      'The First World Leader To Create A YouTube Channel Was The British Prime Minister, Tony Blair Who Made His Account In 2007.',
      'Polar Bears Often Hunt Walruses By Simply Charging At A Group Of Them And Eating The Ones That Were Crushed Or Wounded In The Mass Panic To Escape. Direct Attacks Are Rare.',
      'The Original Xbox Contained Edited Snippets Of Actual Transmissions From The Apollo Missions.',
      'There Is An Insurance Policy Issued Against Alien Abduction. Around 50,000 Policies Have Been Sold, Mainly To Residents Of The U.S. And England.',
      'Medical Errors Are The 6th Leading Cause Of The Death In The U.S.',
      'The Modern Salute Is Believed To Be Derived From The Way In Which French Knights Would Greet Each Other By Lifting The Visors Of Their Helmets.',
      'A Man With Severe OCD And A Phobia Of Germs Attempted To Commit Suicide With A Gun To His Head. Instead Of Killing Him, The Bullet Eliminated His Mental Illness Without Any Other Damage.',
      'One Of The World Trade Centers Was Built To Be 1,776 Feet Tall On Purpose To Reference The Year The Declaration Of Independence Was Signed.',
      'Hugh Jackman Often Will Tell Paparazzi Where He Is When He Goes Home To Australia So They Can Get Their Photos Then Leave Him Alone For The Rest Of His Visit.',
      'Your Tonsils Can Grow Back If There Was Tissue Left Behind During The Removal Process. Sometimes Its Accidental, Other Times Its Left On Purpose.',
      'During The Entire Run Of Gilligans Island, It Was Never Revealed If "Gilligan" Was His First Or Last Name.',
      'When Cellophane Was Invented In 1908, It Was Originally Intended To Be Used To Protect Tablecloths From Wine Spills.'
    ]
    embed = discord.Embed(title="Funfact", color=0xf1c40f)
    embed.add_field(name="Selected fun fact is", value=random.choice(funfacts))
    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(FunFacts(bot))