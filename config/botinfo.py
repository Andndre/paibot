prefix = '_'

# 'command': [
#   'description',
#   'example'
# ]
cmds = {
  f'{prefix}help': [
    'list all my commands',
    '_help'
    ],
  f'{prefix}help <command>' : [
    'show more information about a spesific command',
    '_help ar'
    ],
  f'{prefix}calc <math expression>': [
    'basic calculator',
    '_calc (1+1)+1*0-(3+5)'
    ],
  f'{prefix}hi': [
    'greet me',
    '_hi'
    ],
  f'{prefix}mquiz': [
    'generate a random math quiz',
    '_mquiz'
    ]
}