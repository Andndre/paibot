import os

from discord import Intents
from discord import activity
from discord.ext import commands

# from dotenv import load_dotenv

import config.botinfo as inf

# load_dotenv()

bot = commands.Bot(inf.prefix, activity = activity.Game(name=f'Type {inf.prefix}help for usage!'), help_command = None, intents=Intents.all())

@bot.event
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.load_extension('cogs.help_command')
bot.load_extension('cogs.math_commands')
bot.load_extension('cogs.other_commands')

bot.run(os.environ.get('TOKEN'))
