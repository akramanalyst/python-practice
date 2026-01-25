 # set....
"""
# to create empty set 
grpA = set()

#grpA = { }# type is dictionary.
grpA = {1,2,3,4}
print(grpA)
print(type(grpA))

grpA.add(10)
grpA.remove(4)
print(grpA)


lst = [ 1,2,3,4,5,6,7,8,9,5,4,3]
print(lst)
set1 = set(lst)
print(set1)

"""


# union and intersection:

set1 = { 1,2,3,4,7,9}
set2 = {1,2,3,5,8,10}

print(set1.union(set2))
print(set1.intersection(set2))

set1 = { 1,2,3,4}
set2 = {1,2}

print(set2.issubset(set1))
print(set1.issuperset(set2))
