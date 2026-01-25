"""
python program to create a list of ten numbers by taking input from user 
now  find sum and average of numbers

"""
num = int(input(" Enter number : "))
lst = [ ]
for i in range(0 , num):
	n = int(input(" enter a number  : "))
	lst.append(n)
	print(lst)
s = sum(lst)
print(s)
a = s/num
print(a)
	
