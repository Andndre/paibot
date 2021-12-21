from discord import embeds
from discord.colour import Colour

from config.botinfo import *


def list_all_commands():
  em = embeds.Embed(title='Commands', description=f'All my commands\n\n')
  for k in cmds.keys():
    em.description += f'> **{k}**\n'
  em.description += '\nUse `help <command>` to show information about a specific command\n'
  em.description += '\nReact with <:more:920566095864279090> to show more information'
  em.colour = Colour.blurple()
  return em

def list_all_commands_more():
  em = embeds.Embed(title='Commands', description=f'All my commands')
  for k,v in cmds.items():
    em.add_field(name=k, value=f'```\n{v[0]}\n```', inline=False)
  em.colour = Colour.blurple()
  return em

def help_command(cmd):
  em = embeds.Embed(title=f'Command: {cmd}') 
  em.add_field(name='description:', value=f'```\n{cmds[cmd][0]}\n```', inline=False)
  em.add_field(name='example:', value=f'```\n{cmds[cmd][1]}\n```',inline=False)
  em.colour = Colour.blurple()
  return em

def command_not_found_embed(cmd):
  return embeds.Embed(title='Command not found', description=f'There is no command called {cmd}\n\nuse `{prefix}help` to list all my commands!', colour=Colour.red())

def error_embed(err):
  return embeds.Embed(title='Error', description=f'```\n{err}\n```', colour=Colour.red())
