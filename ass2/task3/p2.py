"""
python program to create a fucntion calc(),write a code to find summation,subtraction,multiplication and division.
and return result in form of list.now test calc() function.

"""
n1 = int(input(" Enter first number : "))
n2 = int(input(" Enter second number : "))

def calc(num1,num2):
	result = [ ]
	sum =  num1+num2
	#print(sum,end = " ")
	result.append(sum)
	
	sub = num1 - num2	
	#print(sub,end = " ")
	result.append(sub)
	
	mul = num1*num2
	#print(mul, end= " ")
	result.append(mul)

	div = num1//num2
	#print(div,end = " ")
	result.append(div) 

	return result 
print(calc(n1,n2))
