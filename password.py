import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

upper1=chr(random.randint(65,90))
upper2=chr(random.randint(65,90)) 
lower1=chr(random.randint(97,122))
lower2=chr(random.randint(97,122))
fancycha1=chr(random.randint(32,64))
fancycha2=chr(random.randint(32,64))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))

password = upper1 + upper2 + lower1 + lower2 + fancycha1 + fancycha2 + digit1 + digit2
password = shuffle(password)

print(password)