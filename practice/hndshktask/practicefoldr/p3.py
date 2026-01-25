#Python Program to find Even Numbers in Range.
even_list = []
odd_list = []

for i in range(1,100):
	if i % 2 == 0:
	
		#print("Even numbers:",i)
 		even_list.append(i)
	if i % 2 != 0:
		odd_list.append(i)
print("Even numbers list fro 1  to 100 is below : ")
print(even_list)
print("Odd Numbers list from 1 to 100 is below  : ")
print(odd_list)	