import asyncio
import datetime
import re

from discord import colour
from discord.colour import Colour
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.context import Context
from discord.message import Message
from utils.calc import calc_
from utils.mquiz import generate_quiz
from config import embeds_

class MathCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(name='calc')
  async def calc(self, ctx: context.Context, *args):
    arg = (''.join(args)).replace('x', '*').replace(':', '/').replace(' ', '')

    result = ''
    err = False
    try:
      result = calc_(arg)
      if re.match(r'[a-zA-Z]', result) != None:
        await ctx.reply(embed=embeds_.error_embed(result))
        err = True
        return
    except:
      await ctx.reply(embed=embeds_.error_embed('Something is wrong with your input, please try to enter the operator and parentheses correctly'))
      return
    finally:
      if err: return
      em = Embed(timestamp=datetime.datetime.utcnow())
      em.add_field(name='Input: ', value=' '.join(arg.split()), inline=False)
      em.add_field(name='Output:',value=result, inline=False)
      em.set_footer(text=f'requested by @{ctx.author.name}')
      em.colour = Colour.blurple()
      await ctx.reply(embed=em)
  
  @commands.command(name='mquiz')
  async def mquiz(self, ctx: Context):
    quiz, ans = generate_quiz()
    message = await ctx.reply(
      embed=Embed(
        title='Quiz', 
        description=
f'''
{ctx.author.mention}, you have 60 seconds to answer:

```
''' + quiz + 
'''
```
'''
      , colour=colour.Colour.blurple()))
    
    def check(m : Message):
      return m.content in ['a','A','b','B','c','C','d','D'] and m.channel == ctx.channel and m.author == ctx.author
    try:
      m : Message = await self.bot.wait_for("message", check = check, timeout = 60)
      if m.content.lower() == ans:
        await m.reply('Congratulations, your answer is correct!')
      else:
        await m.reply(f'Wrong, correct answer is {ans.upper()}')
    except asyncio.TimeoutError:
      await ctx.send("Sorry, you didn't reply in time!")

def setup(bot : commands.Bot):
  bot.add_cog(MathCommands(bot))
