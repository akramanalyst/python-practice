 # recursion
 
#factorial of a number using recursion.
def fact(n):
	if n==1: #base case
		return 1
	else:
		return n*fact(n-1)#5*4*3*2*1 #recursive case
num = int(input(' enter number : ' ))
print(fact(num))