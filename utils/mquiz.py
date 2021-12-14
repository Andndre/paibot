import random

from utils.calc import calc_

def generate_quiz():
  ops = [' + ',' - ',' x ',' : ']
  nums = []
  result = ''
  for n in range(random.randrange(4, 6)):
    nums.append(random.randrange(1, 200))
  result += f'{nums[0]}'
  for n in range(1, len(nums)):
    result += f'{random.choice(ops)}{nums[n]}'
  answer = float(calc_(result.replace(' x ','*').replace(' : ','/')))
  choices = [answer]
  for n in range(4):
    c = answer + random.randrange(-25, 25)
    while c in choices:
      c = answer + random.randrange(-25, 25)
    choices.append(c)
  random.shuffle(choices)
  idx = 0
  for i in range(len(choices)):
    if choices[i] == answer:
      idx = i
      break

  return result + '\n\n' + '\n'.join([chr(n) + '. ' + '{:.2f}'.format(choices[n-97], 2) for n in range(97, 101)]), chr(idx+97)