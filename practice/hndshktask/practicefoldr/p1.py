#Python Program to Check if a Number is Positive, Negative, or 0.

num = int(input("enter the numer to check it."))
'''
if num > 0 : 
	print("positive")
elif num < 0 : 
	print("negative")
else : 
	print("zero")

sign = "positve" if num>0 else "negative"if  num<0 else "zero"
print(sign)
'''
result =lambda num :"positve" if num>0 else "negative"if  num<0 else "zero"
print(result(num))