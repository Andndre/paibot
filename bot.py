import os

from discord import Intents
from discord import Embed, activity
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from dotenv import load_dotenv

import config.botinfo as inf

load_dotenv()
bot = commands.Bot(inf.prefix, activity = activity.Game(name=f'Type {inf.prefix}help for usage!'), help_command = None, intents=Intents.all())
slash = SlashCommand(bot, sync_commands=True)

guild_ids = [919177496669351956]

@slash.slash(name="add", guild_ids=guild_ids, options=[
  create_option(name='first number', required=True),
  create_option(name='second number', required=True)
  ]
)
async def test(ctx: SlashContext):
  embed = Embed(title="Test")
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.load_extension('cogs.help_command')
bot.load_extension('cogs.math_commands')
bot.load_extension('cogs.other_commands')

bot.run(os.getenv('TOKEN'))
