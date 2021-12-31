from discord import embeds
from discord.colour import Colour

from config.botinfo import *


def list_all_commands():
  em = embeds.Embed(title='Commands', description=f'Use `_help <command>` to show more informations about a specific command\n\n')
  for k in cmds.keys():
    em.description += f'> **{k}**\n'
  em.description += '\nUse `help <command>` to show information about a specific command\n'
  em.description += '\nReact with <:more:920566095864279090> to show more information'
  em.colour = Colour.blurple()
  return em

def list_all_commands_more():
  em = embeds.Embed(title='Commands', description=f'Use `_help <command>` to show more informations about a specific command')
  for k,v in cmds.items():
    em.add_field(name=k, value=f'```\ndescription: {v["description"]}\n\nusage: {v["usage"]}\n```', inline=False)
  em.colour = Colour.blurple()
  return em

def help_command(cmd):
  em = embeds.Embed(title=f'Command: {cmd}') 
  em.add_field(name='description:', value=f'```\n{cmds[cmd]["description"]}\n```', inline=False)
  if cmds[cmd]["aliases"] != '':
    em.add_field(name='aliases:', value=f'```\n{", ".join(cmds[cmd]["aliases"])}\n```')
  em.add_field(name='usage:', value=f'```\n{cmds[cmd]["usage"]}\n```',inline=True)
  if cmds[cmd]["example"] != '':
    em.add_field(name='example:', value=f'```\n{cmds[cmd]["example"]}\n```')
  em.colour = Colour.blurple()
  return em

def error_embed(err):
  return embeds.Embed(title='Error', description=f'```\n{err}\n```', colour=Colour.red())

def bot_info(guilds):
  embed =embeds.Embed()
  embed.set_thumbnail(url='https://user-images.githubusercontent.com/81848639/147162613-dfa58c95-a0c8-4cdf-84a8-7d4c4eb4ab0a.jpg')
  embed.title = 'Bot Info'
  embed.add_field(name='Created', value='Saturday, December 11, 2021 21:30:45', inline=False)
  embed.add_field(name='Author', value='<@695390633505849424>', inline=True)
  embed.add_field(name='Invite link', value='[invite me!](https://discord.com/api/oauth2/authorize?client_id=919216307826741269&permissions=137439397952&scope=bot%20applications.commands)', inline=True)
  embed.add_field(name='Servers', value=f'{guilds} servers', inline=False)
  embed.set_footer(text='Use _help for usage!')
  embed.colour = Colour.blurple()
  return embed

def result_embed(res):
  em = embeds.Embed()
  em.add_field(name='Result:',value=res, inline=False)
  em.colour = Colour.blurple()
  return em
