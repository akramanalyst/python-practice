# python program to create dictionary and traverse elements of dictionary using for loop.

mydict = { 1 : 'akram' , 2 : ' four' , 3 : ' lucknow', 4 : 'jamal' }
for k , v in mydict.items():
	print(k,':',v)
	print("   ")
print(mydict.get(2))

"""
no_of_elements = int(input(" Enter no of elements  : "))
mydict = { }
for i in range(no_of_elements):
	key = int(input(" Enter key of elements : "))
	val =  input(" Enter value of elements : ")
	mydict[ key ] = val 
print(mydict)

"""	