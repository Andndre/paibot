import re

ord_a = ord('a')
ord_A = ord('A')

def atbash_(inpt: str) -> str:
  result = ''
  for n in inpt:
    if re.search(r'^[a-zA-Z]+$', n):
      upper = n.isupper()
      c = chr((27 - order(n)) + 96)
      result += c.upper() if upper else c
    else:
      result += n
  return result

def order(char: str) -> int:
  return ord(char.lower())-96

def caesar_make_(character: str, move_to: int, thestr: str) -> str:
  o = order(character) - move_to
  return offset(thestr, o)

def caesar_solve_(character: str, move_to: int, thestr: str) -> str:
  o = move_to - order(character)
  return offset(thestr, o)

def offset(thestr: str, offset: int) -> str:
  if offset == 0: return thestr
  result = ''
  for n in thestr:
    if re.search(r'^[a-zA-Z]+$', n):
      upper = n.isupper()
      new_ord = order(n) + (offset%26)
      while(new_ord <= 0): new_ord += 26
      while(new_ord >= 27): new_ord -= 26
      new_ord += (ord_A-1) if upper else (ord_a-1)
      result += chr(new_ord)
    else:
      result += n
  return result

def nth_word(sentence: str, n: int) -> str:
  res = ''
  for c in sentence:
    if c == ' ':
      n-=1
      if n == 0: break
      continue
    if n == 1: res += c
  return res
