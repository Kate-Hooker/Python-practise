# #string data type

# #literal assignment

# first= "kate"
# last= "hooker"

# # print(type(first))
# # print(type(last) == str)
# # print(isinstance(first, str))

# #constructor function

# # pizza = str("pepperoni")
# # print(type(pizza))
# # print(type(pizza) == str)
# # print(isinstance(pizza, str))

# #concatenation

# fullname = first + " " + last
# print(fullname)
# fullname += "!"
# print(fullname)

# decade="1980"
# print(type(decade))
# print(decade)
# fullname = first + " " + last
# statement = fullname + " was born in the " + decade + "s"
# print(statement)

# # multiple lines

# multilines = """

# This is a weird thing python can do

# I might write some poetry here

# how lovely

# """
# print(multilines)

# #escaping special characters
# # sentance='I\'m a sentance \t What\'s up \n I\'m another sentance'
# # print(sentance)

# #sting methods
# # print(first)
# # print(first.lower())
# # print(first.upper())

# # print(multilines.title())
# # print(multilines.replace("weird", "cool"))
# # print(multilines)
# # print(len(multilines))

# #build a menu
# title= "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + " $1.00".rjust(4))
# print("Murder".ljust(16, ".") + " $14.50".rjust(4))
# print("Bribe".ljust(16, ".") + " $10.00".rjust(4))

# #sting index values (will pull from last saved string aka name)
# print(first[0])

# #use string value -1 to print the last letter of a string
# print(first[-1])
# print(first[-3:-1])

# #some methods return boolean data
# print(first.startswith("k"))
# print(first.endswith("e"))

# #boolean data type
# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# #intege type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# #float type
# gpa = 3.28
# y = float(1.14)
# print(type(gpa))
# print(isinstance(y, float))

# #complex type
# comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# #builty in functions for numbers
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))

# import math
# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))

# #casting a string to a number
# zipcode = "100001"
# zip_value = int(zipcode)
# print(type(zip_value))

# # Error if you attempt to cast incorrect data
# #zip_value = int("new york")
