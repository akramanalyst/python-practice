# python program to find sum of digit of given number.

n = int(input(" Enter the number to find digits sum :  "))
sum=0
while n > 0:
	digit = n%10
	sum = sum+digit
	n=n//10
print(" sum of digit = " , sum)
	
