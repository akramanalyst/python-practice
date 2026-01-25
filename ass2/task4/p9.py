# python rogram to create dictionary by taking input from user now traverse elements of dictionary.
"""

mydict = { } 
mydict.update({ 1: 'akram', 2: ' naeem ', 3: ' arif ' }) # to update dictionary with multiple keys and values.
print(mydict)
print("   ")
print(mydict.get(3)) # to get the value from dictionary using passing the key.

"""
num = int(input(" Enter the no of elements : "))
mydict = { }
for i in range(num):
	key = input(" Enter the key of elements  : ")
	val = input( ' Enter the values of elements :  ')
	mydict[key] = val
print("      ")
print(mydict)