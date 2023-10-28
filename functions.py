#a reuseable bock of code that runs verytime you call kit

def hello():
  print("hello")

hello()
# will print hello

def sum(num1, num2):
  if (type(num1)is not int or type(num2) is not int):
    return
  print(num1 + num2)

sum(1, 2)
# will print 3

total = sum(9, 1)
print(total)
# will print 10

def multiple_items(*args):
  print(args)
  print(type(args))

multiple_items("Shovel", "Lime", "Duct Tape")

def multiple_named_args(**kwargs):
  print(kwargs)
  print(type(kwargs))

multiple_named_args(a="Shovel", b="Lime", c="Duct Tape")
#prints {'a': 'Shovel', 'b': 'Lime', 'c': 'Duct Tape'} <class 'dict'>