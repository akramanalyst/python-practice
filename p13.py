  
n1 = int(input(" enter 1st  number : "))
n2 = int (input(" enter 2nd number : "))

# addition of two numbers.

def  add(num1,num2):
	sum = num1+num2
	print("sum = ",sum ,end=" , ")
#add(n1,n2)

#subtraction of two numbers.

def sub(num1,num2):
	sub=num1-num2
	print("sub = ",sub,end=" , ")
#sub(n1,n2)

#multiplication of two numbers.

def mul(num1,num2):
	mul = num1*num2
	print("multiplication : ",mul,end=" , ")
#mul(n1,n2)

# division of two numbers.

def div(num1,num2):
	div = num1//num2
	print("division = :", div,end=" , ")
#div(n1,n2)

add(n1,n2)
sub(n1,n2)
mul(n1,n2)
div(n1,n2)