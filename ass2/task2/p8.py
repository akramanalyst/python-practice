# python program to find factorial of given number.

n = int(input(" Enter the number to find factorial : "))
fact = 1
i=1
while i<=n:
	fact = fact*i
	print(fact)
	i+=1