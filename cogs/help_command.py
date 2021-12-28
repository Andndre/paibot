import asyncio

from config import botinfo, embeds_
from discord import embeds
from discord.colour import Colour
from discord.abc import User
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.message import Message
from discord.reaction import Reaction

class HelpCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='help')
  async def help(self, ctx: Context, *args):
    cmd = ' '.join(args)
    if cmd.strip() == '':
      if ctx.guild:
        message :Message = await ctx.send(embed=embeds_.list_all_commands())
        await message.add_reaction(emoji='<:more:920566095864279090>')
        def check(r : Reaction, u: User):
          return str(r.emoji) == '<:more:920566095864279090>' and u == ctx.author
        try:
          reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=60)
          await message.edit(embed=embeds_.list_all_commands_more())
        except asyncio.TimeoutError:
          pass
        except Exception as e:
          await ctx.send(embed=embeds_.error_embed(str(e)))
      else:
        message :Message = await ctx.send(embed=embeds_.list_all_commands_more())
      return
    for n in botinfo.cmds.keys():
      if cmd.strip() == n:
        await ctx.send(embed=embeds_.help_command(n))
        return
    await ctx.send(embed=embeds_.command_not_found_embed(cmd))
  @commands.command(aliases=['about'])
  async def botinfo(self, ctx: Context):
    embed = embeds_.bot_info(len(self.bot.guilds))
    await ctx.send(embed=embed)

def setup(bot : commands.Bot):
  bot.add_cog(HelpCommand(bot))
