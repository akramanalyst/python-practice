#wap to check number is primeor not .
num = int(input("enter the number to check prime or not "))
count = 0
for i in range(1,num+1):
	if num % i == 0:
		count = count+1

if count ==2:
	
	print("entered number is prime:")
else:

	print("number is not prime")