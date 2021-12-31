import traceback
from config.botinfo import cmds
from config.embeds_ import error_embed, result_embed
from discord.ext import commands
from discord.ext.commands.context import Context
from utils.string import (atbash_, caesar_make_, caesar_solve_,
                                       nth_word)


class StringManipulatonCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=cmds['atbash']['aliases'])
  async def atbash(self, ctx: Context, *, inpt):
    inpt = inpt.replace('\\n', '\n').replace('<br>', '\n')
    await ctx.send(embed=result_embed(atbash_(inpt)))
  
  @commands.command(aliases=cmds['caesar_solve']['aliases'])
  async def caesar_solve(self, ctx: Context, *, inpt):
    try:
      inpt = inpt.replace('\\n', '\n').replace('<br>', '\n')
      fw = nth_word(inpt, 1)
      arg2 = fw.split('=')
      thestr = inpt[len(fw)+1:]
      await ctx.send(embed=result_embed(caesar_solve_(arg2[0], int(arg2[1]), thestr).replace('\n ', '\n').strip()))
    except:
      await ctx.send(embed=error_embed('Invalid input!'))

  @commands.command(aliases=cmds['caesar_make']['aliases'])
  async def caesar_make(self, ctx: Context, *, inpt):
    try:
      inpt = inpt.replace('\\n', '\n').replace('<br>', '\n')
      fw = nth_word(inpt, 1)
      arg = fw.split('=')
      thestr = inpt[len(fw)+1:]
      arg1 = int(arg[1])
      await ctx.send(embed=result_embed(caesar_make_(arg[0], arg1, thestr).replace('\n ', '\n').strip()))
    except:
      await ctx.send(embed=error_embed(f'Invalid input!\n\n{traceback.format_exc()}'))

def setup(bot : commands.Bot):
  bot.add_cog(StringManipulatonCommands(bot))
