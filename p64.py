# iterator
'''
lst = [1,2,3,4,5,6,7,8]
print(lst[0])

it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print(next(it))
print(next(it))
'''
#Genarator

def simple_generator(n):
	for i in range(1,n+1):
		yield i
gen =simple_generator(10)
#print(next(gen))
#print(next(gen))

s = 0
for i in gen:
	s = s+i
print(s)
