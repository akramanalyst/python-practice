"""
python program to create a function search().in search() pass two parameters firsta list of ten numbers and 
second a number to search if number is present in list return index of list otherwise return false.  
"""
n = int(input(" Enter the number : "))
my_list = [ 1,3,2 ,5,6,8,4,7,9 , 10 ] 
def search(my_list,num):
	print(my_list)
	print(type(my_list))
	print(len(my_list))

	#my_list.reverse()
	#print(my_list)
	print(max(my_list))
	print(min(my_list))
	print(my_list[-1])


	if  n in my_list:
		print(" number is present in list  .")
		print(my_list.index(num))
	else:
		print(" number is not present in list .")
search(my_list,n)