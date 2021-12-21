import asyncio
import re
import traceback

from config import embeds_
from discord.colour import Colour
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.context import Context
from discord.message import Message
from utils.calc import calc_
from utils.mquiz import generate_quiz


class MathCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(name='calc')
  async def calc(self, ctx: context.Context, *args):
    arg = (''.join(args))
    result = ''
    try:
      result, err = calc_(arg)
      if err:
        await ctx.reply(embed=embeds_.error_embed(result))
        return
      em = Embed()
      em.add_field(name='Result:',value=result, inline=False)
      em.colour = Colour.blurple()
      await ctx.reply(embed=em)
    except Exception as e:
      traceback.print_exc()
      await ctx.reply(embed=embeds_.error_embed(f'Something is wrong with your input, please try to enter the operator and parentheses correctly\n\n"{str(e)}"'))
      return
  
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
      , colour=Colour.blurple()))
    
    def check(m : Message):
      return (
        m.content.lower().strip() in ['a','b','c','d'] 
          and m.channel == ctx.channel 
          and m.author == ctx.author
        )
    try:
      m : Message = await self.bot.wait_for('message', check = check, timeout = 60)
      if m.content.lower() == ans:
        await m.reply('Congratulations, your answer is correct!')
      else:
        await m.reply(f'Wrong, correct answer is {ans.upper()}')
    except asyncio.TimeoutError:
      await ctx.send("Sorry, you didn't reply in time!")

def setup(bot : commands.Bot):
  bot.add_cog(MathCommands(bot))
