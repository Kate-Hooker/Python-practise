users = ['Kate', 'James', 'Aggy']
data = ['Kate', 42, True]
emptylist = []

print("Kate" in users)
# will print True because it is in the list

print(users [0])
# will print Kate

print(users[-1])
# will print Aggy

print(users.index('James'))
# will print 1

print(users[0:2])
# will print ['Kate', 'James']

print(users[-3:-1])
# will print ['James', 'Aggy']

print(len(data))
# will print 3

users.append('Elsa')
print(users)
# will print ['Kate', 'James', 'Aggy', 'Elsa']

users += ['Hammy']
print(users)
# will print ['Kate', 'James', 'Aggy', 'Elsa', 'Hammy']

users.remove('Aggy')
print(users)
# will print ['Kate', 'James', 'Elsa', 'Hammy']

users.extend(['Pedro', 'Marty'])
print(users)
# will print ['Kate', 'James', 'Elsa', 'Hammy', 'Pedro', 'Marty']



users.sort()
print(users)
# will print ['Elsa', 'Hammy', 'James', 'Kate', 'Marty', 'Pedro']

users.reverse()
print(users)
# will print ['Pedro', 'Marty', 'Kate', 'James', 'Elsa', 'Hammy']

users.insert(0, 'Peter')
print(users)
# will print ['Peter', 'Pedro', 'Marty', 'Kate', 'James', 'Elsa', 'Hammy']

users.pop()
print(users)
# will print ['Peter', 'Pedro', 'Marty', 'Kate', 'James', 'Elsa']

users[2:2] = ['Vivacious', 'Adore']
print(users)
# will print ['Peter', 'Pedro', 'Vivacious', 'Adore', 'Kate', 'James', 'Elsa']

users[1:4] = ['Madrid', 'Paris']
print(users)
# will print ['Peter', 'Madrid', 'Paris', 'Vivacious', 'Adore', 'Kate', 'James', 'Elsa']

users.remove('Madrid', 'Elsa')
print(users)
# will print ['Peter', 'Paris', 'Vivacious', 'Adore', 'Kate', 'James']

users.delete[0]
print(users)
# will print ['Paris', 'Vivacious', 'Adore', 'Kate', 'James']

users.clear()
print(users)
# will print [] 

users.extend('Anna', 'Jojo', 'Lance')
print(users)
# will print ['Anna', 'Jojo', 'Lance']

nums = [11,6,7,8,9,10]
nums.reverse()
print(nums)
# will print [10, 9, 8, 7, 6, 11]

nums.sort(reverse = True)
print(nums)
# will print [11, 10, 9, 8, 7, 6]

# Tuples
mytuple = tuple(('Nancy', True, 42))
print(mytuple.type)
# will print <class 'tuple'>

# Tuples cannot be edited - to edit start a new variable
newlist = list(mytuple)
print(newlist)
# will print ['Nancy', True, 42]
newlist.append('Paula')
newtuple = tuple(newlist)
print(newtuple)
# will print ('Nancy', True, 42, 'Paula')

