from discord.ext import commands
from discord.ext.commands.context import Context
import re

from config.embeds_ import error_embed, result_embed

ord_a = ord('a')
ord_A = ord('A')

def order(char: str) -> int:
  return ord(char.lower())-96

def caesar_make(character: str, move_to: int, thestr: str) -> str:
  o = order(character) - move_to
  return offset(thestr, o)

def caesar_solve(character: str, move_to: int, thestr: str) -> str:
  o = move_to - order(character)
  return offset(thestr, o)

def offset(thestr: str, offset: int) -> str:
  if offset == 0: return thestr
  result = ''
  for n in thestr:
    if re.search(r'^[a-zA-Z]+$', n):
      upper = n.isupper()
      new_ord = order(n) + offset
      if(new_ord <= 0): new_ord += 26
      elif(new_ord >= 27): new_ord -= 26
      new_ord += (ord_A-1) if upper else (ord_a-1)
      result += chr(new_ord)
    else:
      result += n
  return result

def nth_word(sentence: str, n: int) -> str:
  res = ''
  for c in sentence:
    if c == ' ':
      n-=1
      if n == 0: break
      continue
    if n == 1: res += c
  return res

class StringManipulatonCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='atbash')
  async def atbash(self, ctx: Context, *, inpt):
    inpt = inpt.replace('\\n', '\n')
    result = ''
    for n in inpt:
      if re.search(r'^[a-zA-Z]+$', n):
        upper = n.isupper()
        c = chr((27 - order(n)) + 96)
        result += c.upper() if upper else c
      else:
        result += n
    await ctx.send(embed=result_embed(result))
  
  @commands.command(name='caesar_solve')
  async def caesar_solve(self, ctx: Context, *, inpt):
    try:
      inpt = inpt.replace('\\n', '\n')
      fw = nth_word(inpt, 1)
      arg2 = fw.split('=')
      thestr = inpt[len(fw)+1:]
      await ctx.send(embed=result_embed(caesar_solve(arg2[0], int(arg2[1]), thestr).replace('\n ', '\n').strip()))
    except:
      await ctx.send(embed=error_embed('Invalid input!'))

  @commands.command(name='caesar_make')
  async def caesar_make(self, ctx: Context, *, inpt):
    try:
      inpt = inpt.replace('\\n', '\n')
      fw = nth_word(inpt, 1)
      arg = fw.split('=')
      thestr = inpt[len(fw)+1:]
      await ctx.send(embed=result_embed(caesar_make(arg[0], int(arg[1]), thestr).replace('\n ', '\n').strip()))
    except:
      await ctx.send(embed=error_embed('Invalid input!'))

def setup(bot : commands.Bot):
  bot.add_cog(StringManipulatonCommands(bot))