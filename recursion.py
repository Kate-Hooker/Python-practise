# a rcursive function is a function that calls itself over and over again

def add_one(num):
  if (num >= 9):
    return num + 1
  #if this if statement is true then it will return num + 1 and end the function
  #If the condition in the if statement is False, this line calculates num + 1 and assigns the result to a variable named total.
  total = num + 1
  print(total)

  return add_one(total)
  
add_one(0)
#will print the numbers one through 9

mynewtotal = add_one(0)
print(mynewtotal)

#this can also be done with a loop
value = 0
while value <= 9:
  print(value)
  value += 1

print(value)

