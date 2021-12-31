import asyncio
import traceback
from random import randint

from config.embeds_ import error_embed
from config.botinfo import cmds
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member
from discord.message import Message


class OtherCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=cmds['hi']['aliases'])
  async def hi(self, ctx: Context):
    author : Member = ctx.author
    await ctx.send(f'Hello to you too {author.mention}👋')
  
  @commands.command(aliases=cmds['rps']['aliases'])
  async def rps(self, ctx: Context):
    message = await ctx.send('rock(r)/paper(p)/scissors(s)')

    def check(m: Message):
      return m.author == ctx.author and m.content.lower() in ['rock', 'r', 'paper', 'p', 'scissors', 's']
    try:
      msg_ : Message = await self.bot.wait_for('message', check = check, timeout=60)
      bot_input = ['rock', 'paper', 'scissors'][randint(0, 2)]

      user_input = msg_.content.lower()

      msg = ''
      if user_input == 'scissors' or user_input == 's':
        if bot_input == 'paper':
          msg = 'You win!'
        elif bot_input == 'rock':
          msg = 'You lose!'
      elif user_input == 'paper' or user_input == 'p':
        if bot_input == 'scissors':
          msg = 'You lose!'
        elif bot_input == 'rock':
          msg = 'You win!'
      elif user_input == 'rock' or user_input == 'r':
        if bot_input == 'paper':
          msg = 'You lose!'
        elif bot_input == 'scissors':
          msg = 'You win!'
      if msg == '':
        msg = 'draw!'
      await ctx.send(bot_input + '\n' + msg)
    except asyncio.TimeoutError:
      pass
    except Exception as e:
      await ctx.send(embed=error_embed(str(e) + '\n\n' + traceback.format_exc()))

def setup(bot : commands.Bot):
  bot.add_cog(OtherCommands(bot))
