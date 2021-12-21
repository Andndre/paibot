import re
from typing import Any, Tuple

# FUNC: helper
def findnth(string : str, target : str, nth : int) -> str:
    parts= string.split(target, nth+1)
    if len(parts)<=nth+1:
      return -1
    return len(string)-len(parts[-1])-len(target)

# FUNC: main
def calc_(mth : str) -> Tuple[Any, bool]:
  if re.search(r'[^0-9+\-*/:()Xx^\s]', mth):
    return 'Accepts only numbers and symbols `+ - * x : / ( ) ^`', True
  op = mth.count('(')
  cl = mth.count(')')
  if op != cl:
    opcl = "opening" if op > cl else "closing"
    return f'There are too many {opcl} brackets somewhere', True
  return str(eval(validate(mth))), False

# FUNC: step1
def validate(mth : str) -> str:
  mth = (
    mth
    .replace('++', '+')
    .replace('-+', '-')
    .replace('+-', '-')
    .replace('--', '+')
    .replace('^', '**')
    .replace('x', '*')
    .replace('X', '*')
    .replace(':', '/')
  )

  # add missing * before ( or after )
  j = 0
  operators = ['+','-','*','/']
  while(True):
    # Here we check for the '(' and ')' together because 
    # the number of occurrences is the same,
    # unless the input is invalid
    i = findnth(mth, '(', j)
    if i-1 in [-1, -2]: break
    # founded '(', checks if the previous 
    # character is not an 'operator' and '('
    if mth[i-1] not in operators and mth[i-1] != '(':
      # insert '*' at i
      mth = mth[:i] + '*' + mth[i:]
    i = findnth(mth, ')', j)
    # check if i+1 is the end of mth string
    if i+1 == len(mth): break
    # founded ')', checks if the next 
    # character is not an 'operator' and ')'
    if mth[i+1] not in operators and mth[i+1] != ')':
      # insert '*' at i+1
      mth = mth[:i+1] + '*' + mth[i+1:]
    j+=1
  return mth
