#Python Programs for Summing Even Numbers from 1 to n.
n = int(input("Enter the value of n : "))
even_list = []

summ = 0 
for i in range (1, n):
	if i % 2 == 0:
		even_list.append(i)
		summ =summ+i
print(even_list)
print(summ) 
print("using sum () function ")
print(sum(even_list))
