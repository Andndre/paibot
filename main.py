import os

from discord import Intents
from discord import activity
from discord.ext import commands

# from dotenv import load_dotenv

# load_dotenv()

bot = commands.Bot('_', activity = activity.Game(name=f'Type _help for usage!'), help_command = None, intents=Intents.all(), owner_id=695390633505849424)

@bot.event
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.load_extension('cogs.help_command')
bot.load_extension('cogs.math_commands')
bot.load_extension('cogs.other_commands')
bot.load_extension('cogs.string_manipulation_cmds')

bot.run(os.environ.get('TOKEN'))
# bot.run(os.getenv('TOKEN'))
