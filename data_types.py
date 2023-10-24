#string data type

#literal assignment

first= "kate"
last= "hooker"

# print(type(first))
# print(type(last) == str)
# print(isinstance(first, str))

#constructor function

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#concatenation

fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

decade="1980"
print(type(decade))
print(decade)
fullname = first + " " + last
statement = fullname + " was born in the " + decade + "s"
print(statement)

# multiple lines

multilines = """

This is a weird thing python can do

I might write some poetry here

how lovely

"""
print(multilines)

#escaping special characters
sentance='I\'m a sentance \t What\'s up \n I\'m another sentance'
print(sentance)

#sting methods
print(first)
print(first.lower())
