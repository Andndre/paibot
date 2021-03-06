import asyncio
import traceback

from config import embeds_
from config.botinfo import cmds
from discord.colour import Colour
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.context import Context
from discord.message import Message
from utils.calc import calc_, get_calc_result
from utils.mquiz import generate_quiz


class MathCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=cmds['calc']['aliases'])
  async def calc(self, ctx: context.Context, *args):
    arg = (''.join(args))
    result = ''
    try:
      result, err = calc_(arg)
      if err:
        await ctx.send(embed=embeds_.error_embed(result))
        return
      em = Embed()
      em.add_field(name='Result:',value=result, inline=False)
      em.colour = Colour.blurple()
      msg : Message = await ctx.send(embed=em)

      def check(before, after):
        return after == ctx.message
      while True:
        before, after = await self.bot.wait_for('message_edit', check=check, timeout=200)
        await msg.edit(embed=get_calc_result(ctx.message.content.replace('_calculator', '').replace('_calc', '')))
    except asyncio.TimeoutError:
      pass
    except Exception as e:
      await msg.delete()
      traceback.print_exc()
      await ctx.send(embed=embeds_.error_embed(f'Something is wrong with your input\ntry: remove unnecessary brackets\n\n"{str(e)}"\n\nevent stopped'))
      return
  
  @commands.command(aliases=cmds['mquiz']['aliases'])
  async def mquiz(self, ctx: Context):
    quiz, ans = generate_quiz()
    message = await ctx.send(
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
        m.content.lower().strip() in ['a','b','c','d','e'] 
          and m.channel == ctx.channel 
          and m.author == ctx.author
        )
    try:
      m : Message = await self.bot.wait_for('message', check = check, timeout = 60)
      if m.content.lower() == ans:
        await ctx.send('Congratulations, your answer is correct!')
      else:
        await ctx.send(f'Wrong, correct answer is {ans.upper()}')
    except asyncio.TimeoutError:
      await ctx.send("Sorry, you didn't reply in time!")

def setup(bot : commands.Bot):
  bot.add_cog(MathCommands(bot))
