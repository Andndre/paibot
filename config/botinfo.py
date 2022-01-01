# 'command': {
#   'aliases' -> list
#   'description', -> str
#   'usage', -> str
#   'example' -> str
# }
cmds = {
  'help': {
    'aliases': [],
    'description': 'list all my commands',
    'usage': '_help, _help <command>',
    'example': ''
  },
  'botinfo': {
    'aliases': ['about'],
    'description': 'Sends an embed with basic information about the bot',
    'usage': '_botinfo, _about',
    'example': ''
  },
  'calc': {
    'aliases': ['calculator', 'cal'],
    'description': 'basic calculator',
    'usage': '_calc <math>, _calculator <math>',
    'example': '_calc 1/(-(5(4-(57))-6))x4'
  },
  'hi': {
    'aliases': ['hello'],
    'description': 'greet me',
    'usage': '_hi, _hello',
    'example': ''
  },
  'mquiz': {
    'aliases': ['math_quiz', 'mq'],
    'description': 'generate a random math quiz',
    'usage': '_mquiz, _math_quiz',
    'example': ''
  },
  'rps':{
    'aliases': ['rock_paper_scissors'],
    'description': 'play rock paper scissors',
    'usage': '_rps, _rock_paper_scissors',
    'example': ''
  },
  'atbash': {
    'aliases': ['atb'],
    'description': 'converts input into atbash\ni.e. A --> Z, B --> Y, C --> X, etc..',
    'usage': '_atbash <input-multi-line>',
    'example': '_atbash hello world\nOut: svool dliow'
  },
  'caesar_make': {
    'aliases': ['cm'],
    'description': 'make caesar puzzle (panda language) that can be solved by offsetting <char> to <move to>',
    'usage': '_caesar_make <char>=<move_to> <input-multi-line>',
    'example': '_caesar_make k=5 hello world\nOut: nkrru cuxrj'
  },
  'caesar_solve': {
    'aliases': ['cs'],
    'description': 'solve caesar_puzle (panda language) by offsetting <char> to <move to>',
    'usage': '_caesar_solve <char>=<move_to> <input-multi-line>',
    'example': '_caesar_solve k=5 nkrru cuxrj\nOut: hello world'
  }
}


emojis = {
  'more': '<:more:920566095864279090>'
}
