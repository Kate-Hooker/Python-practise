# while loops executed a block of code as long as the condition is true

# value = 1
# while value <10:
#   print(value)
#   if value == 5:
#     break
#   value += 1
# will print 1 through 5 then stop

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to " + str(value))

names = ["Kate", "James", "Aggy"]
#in this example x represents any name in the list
for x in names:
    print(x)
#this iterates through the list and prints each name

for x in "Piglet":
    print(x)
#this iterates through the string and prints each letter

for x in names: 
    if x == "James":
        break
    print(x)
#prints Kate

for x in names: 
    if x == "James":
        continue
    print(x)
#prints Kate, Aggy

for x in range(4):
    print(x)
#will print 0, 1, 2, 3

#to start at the second number and end before the fourth
for x in range(2, 4):
    print(x)
#will print 2, 3

#to count from 0 to 100 in increments of 5
for x in range(0, 101, 5):
    print(x)




