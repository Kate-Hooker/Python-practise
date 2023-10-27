band {
  "vocals": "Scum",
  "bass": "Twisted Nightmare",
  "drums": "Pigface"
}

band2 = dict(vocals="Scuzza", bass="Dr Doom", drums="Krusty")

print(band["vocals"])
# will print Scum

print(band2(type))
# will print <class 'dict'>

print(band2.get("vocals"))
# will print Scuzza

print(band.values)
# will print ['Scum', 'Twisted Nightmare', 'Pigface']

print(band2.keys)
# will print ['vocals', 'bass', 'drums']

print(band.items)
# will print [('vocals', 'Scum'), ('bass', 'Twisted Nightmare'), ('drums', 'Pigface')]

# if you need to verify the key exisits
print("drums" in band)
# will print True

# changing values in arrays
band["vocals"] = "Big Stanky"
print(band.objects)
# will print ['Big Stanky', 'Twisted Nightmare', 'Pigface']
band["bass"] = "Butch Slashidy"
print(band.objects)
# will print ['Big Stanky', 'Butch Slashidy', 'Pigface']
band.update({"harmonica": "Mace"})
print(band)
# will print {'vocals': 'Big Stanky', 'bass': 'Butch Slashidy', 'drums': 'Pigface', 'harmonica': 'Mace'}

ejectedmember =band.pop("harmonica")
print(ejectedmember)
# will print Mace
print(band.objects)
# will print ['Big Stanky', 'Butch Slashidy', 'Pigface']

band["Peggy Sue"] = "triangle"
print(band.objects)
# will print ['Big Stanky', 'Butch Slashidy', 'Pigface', 'Peggy Sue']

#pop item will take out whatever was added last
print(band.popitem())
# will print 'Peggy Sue'
print(band.objects)
# will print ['Big Stanky', 'Butch Slashidy', 'Pigface']

del band2
print(band2)
# will print None

#nested dictionaries - when a dictionairy is nested in another dictionairy

member1 = {
  "name": "Killa Flea",
  "instrument": "lead guitar"
}
member2 = {
  "name": "Colon Ferral",
  "instrument": "Tambourine"
}

newband= {
  "member1": member1,
  "member2": member2
}
print(newband)
# will print {'member1': {'name': 'Killa Flea', 'instrument': 'lead guitar'}, 'member2': {'name': 'Colon Ferral', 'instrument': 'Tambourine'}}

print(newband["member2"]["instrument"])
# will print Tambourine

# sets

nums = {1.0, 2.0, 3.0, 4.0, 5.0}
print(nums)
# will print {1.0, 2.0, 3.0, 4.0, 5.0}  

nums2 = set([6, 3, 11])
print(nums2)
# will print {6, 3, 11}
print(type(nums2))
# will print <class 'set'>
print(len(nums))
# will print 5

#sets do not allow duplicates
set3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(set3)
# will print {1, 2, 3, 4, 5}

#add a number to a set
set3 = set3.add(6)
print(set3)
# will print {1, 2, 3, 4, 5, 6}

morenums = {7, 8, 9, 10}
set3.update(morenums)
print(set3)
# will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}





