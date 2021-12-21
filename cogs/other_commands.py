from discord import embeds
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member


class OtherCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(name='hi')
  async def hello(self, ctx: Context):
    author : Member = ctx.author
    await ctx.reply(f'Hello to you too {author.mention}👋')

def setup(bot : commands.Bot):
  bot.add_cog(OtherCommands(bot))

# 1-magic-shell
