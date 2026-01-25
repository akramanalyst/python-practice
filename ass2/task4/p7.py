#program to create set of ten numbers bytaking input from users.now traverse set elements.

my_set = set()
my_list = [ ]
n = int(input(" Enter number : "))
for i in range(0,n):
	elements = int(input("enter sets elements : "))
	my_set.add(elements)
	print(my_set)
	my_list = list(my_set)
	print(my_list)

#print(my_list[0])
#print(my_list[1])
#print(my_list[2])
for item in my_set:
	print(item)