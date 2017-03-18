def reverse (string):
  temp = ''

  for i in reversed(string):
    temp += i

  return temp

def eval_str (string):
  return str(eval(string))
