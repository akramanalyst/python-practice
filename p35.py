#list_comprehension
#lambda function
#filter function
#map function



'''
# expression 

num = 6
print('even number : ' if num%2==0 else "odd")


#list comprehension

#[ expression for item in iterable if condition]

lst = [1,2,3,4,5]

sq = [n**2 for n in lst]
print(lst)
print(sq)
'''
'''

#filter function filter() used to select subset from a collection based on a function return type.
numbers =[1,2,3,4,5,6,7,8,9,10]
def is_even(n):
	return n%2==0
def is_odd(n):
	return n%2==1
even_numbers = list(filter(is_even,numbers))
odd_numbers=list(filter(is_odd,numbers))

print(even_numbers)
print(odd_numbers)



#map()
#used to perform operation on each elements of collection and return new collection. 
numbers = [1,2,3,4,5,6,7,8,9,10]
def sq(n):
	return n**2
squared = list(map(sq,numbers))
print(squared)

dict1 = {
	'1001' : 23,
	'1002' :25
}
for k ,v in dict1.items():
	print(k,v)
#adding
dict1['1003']=33
dict1.update({'1004':34,'1005':36})

#get
print(dict1['1002'])

'''

stu = { 
	'ariz':"mohd.ariz",
	'anurag':"anurag he h",
	'akram':"akram jamal"
}
print(stu)
del stu['ariz']
print(stu)

stu.clear()
print(stu)

