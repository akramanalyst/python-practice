# python program to print febanacci series ,where value n entered by user.

"""
n = int(input(" Enter a number : ")) 
x = 0
y = 1
feb = 0
print(x)
print(y)
while feb<n: 
	feb = x+y
	print(feb)
	x = y
	y = feb

"""
n = int(input(" enter a number : "))
num1 = 0
num2 = 1
feb = 0
print(num1)
print(num2)

for i in range(1,n-1):
	feb = num1+num2
	print(feb)
	num1 =  num2
	num2 = feb
