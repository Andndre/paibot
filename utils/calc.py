import re
from typing import Any, Tuple

def calc_(mth : str) -> Tuple[Any, bool]:
  if re.search(r'[^0-9+\-*/:()Xx^.,\s]', mth):
    return 'Accepts only numbers and symbols `+ - * x : / ( ) ^ . ,`', True
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
    .replace(',', '.')
    .replace(' ', '')
  )
  op = mth.count('(')
  cl = mth.count(')')
  if op != cl:
    opcl = "opening" if op > cl else "closing"
    return f'There are too many {opcl} brackets somewhere', True
  step1 = validate(mth)
  # print('step 1:',step1)
  step2 = calc_2(step1.replace(' ', ''))
  # print('step 2:',step2)
  return step2, False

def validate(mth : str) -> str:

  # add missing * before ( or after )
  j = 1
  operators = ['+','-','*','/', '^']
  while(True):
    if j == len(mth)-1:
      break
    if mth[j] == '(':
      if mth[j-1] not in operators and mth[j-1] != '(':
        # insert '*' at i
        mth = mth[:j] + '*' + mth[j:]
    elif mth[j] == ')':
      if mth[j+1] not in operators and mth[j+1] != ')':
        # insert '*' at i+1
        mth = mth[:j+1] + '*' + mth[j+1:]
    j+=1
  return mth

def calc_2(mth : str):

  # Calculate

  # this variable will store all mth inside a brackets, 
  # then computed by this function again (if it has bracket pair)
  # recursively until the braces is gone
  tmp = ''
  final = ''
  unclosed = 0
  got_brace = False
  for n in mth:
    if n == '(':
      if got_brace:
        tmp += '('
      got_brace = True
      unclosed += 1
      continue
    if n == ')':
      unclosed -= 1
      if got_brace:
        if unclosed == 0:
          expanded = calc_2(tmp)
          final += expanded
          got_brace = False
          tmp = ''
        else:
          tmp += ')'
      continue
    if got_brace:
      tmp += n
    else:
      final += n

  # print('calculating', final)

  # after the braces is gone, we finally can 
  # evaluate the result using eval function
  return str(eval(final))
