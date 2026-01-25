"""
 python program to create five students name by taking input from user,
 and perform ascending and descending order .

"""
num = int(input(" Enter no .of students : "))
std_list = [ ] 
for i in range(num):

	students = input(" enter 1 - 5  students name : ")
	std_list.append(students)
	print(std_list)
	#print(" Ascending order : ")
	std_list.sort()
	desc_order = std_list[ :: -1 ]
	print(desc_order)
	