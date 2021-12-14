import re

def findnth(s, m, n):
    parts= s.split(m, n+1)
    if len(parts)<=n+1:
        return -1
    return len(s)-len(parts[-1])-len(m)

# FUNC: main
def calc_(mth):
  # if mth.count('(') == 0: return eval(mth)
  if re.match(r'^[^0-9*+\-/()\s]*$', mth) != None:
    return 'Accepts only numbers and symbols `+ - * x : / ( )`'
  if mth.count('(') != mth.count(')'):
    opcl = "opening" if mth.count("(") > mth.count(")") else "closing"
    return f'There are too many {opcl} brackets somewhere'
  mth = calc_1(mth)
  return calc_2(mth)

# FUNC: step 1
def calc_1(mth):
  
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

# FUNC: step 2
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