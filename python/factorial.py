N = None
i = None
Result = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


N = float(text_prompt('input N'))
if N < 0:
  print('N can not be less zerro')
else:
  i = 0
  Result = 1
  for count in range(int(N)):
    i = i + 1
    Result = Result * i
  print(Result)
  print 'Congratulations'