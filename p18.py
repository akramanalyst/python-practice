# user defined list

"""
numbers = [ ]
for i in range(5):
	n = int(input("enter elements : "))
	numbers.insert(i,n)
	#numbers.append(n)
print(numbers)

"""
"""
#remove() function to remove elements.

lst = [ 12,23,45,56,12] 
#lst.remove(12) #remove first element.
print(lst)

lst.pop()# remove last occurence .
print(lst)
lst.pop(0)# remove first occurence
print(lst)

lst.clear()
print(lst)
"""

"""
# sum of list.

lst = [ 2,1,3,5 ,4]
print(lst)
s = sum(lst)

print("sum = ",s)

print("Max = ",max(lst)) # max value
print("Min = ", min(lst))# min value


lst.sort()
print(lst)


lst.reverse()
print(lst)

"""
#slicing of list

lst = [ 1,3,4,7,9]
print(lst[ 0:3])
print(lst[ 0:5:2])

print(lst[ :: -1])

