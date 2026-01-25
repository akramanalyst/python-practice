# python program to check number is prime or not.

num = int(input("Enter a number to check it is prime or not : "))
c=0
for i in range(1, num+1):
	if num%i==0:
		c=c+1
if c==2:

	print("number is  prime: ")
else:

	print(" Enter nmber is not prime : ")