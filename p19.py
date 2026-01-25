# tuple 
"""
tup = (1,2,3,4)
print(tup)
print(type(tup))
print(tup[0])
print(tup[-1])
for t in tup:
	print(t)

"""
tup1 = tuple()
lst = [ ]
for i in range(5):
	n = int(input(" enter element : "))
	print("   ")
	lst.append(n)
	print(lst)
	print("     ")
tup1 = tuple(lst)
print(tup1)