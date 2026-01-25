#Python Programs to Check if a Number is Odd or Even.
'''
num = int(input("Enter the number : ") )

if num % 2 == 0:
	print("number is Even ")
else :
	print("number is odd")

even_number = lambda num :  num %2 ==0 
print(even_number(num))

even_number = "even" if num % 2 == 0 else "odd"
print(even_number)

def even_number(num):
	if num % 2 == 0 :
		print("Entered number is even .")
	else : 
		print("Entered number is odd .")
even_number(num)
'''
numbers = [1,2,3,44,55,66,666,8888,9,8,10,15,23,24,18,20,200,333]
def even_numbers(n):
	if n % 2 == 0:
		return True
		
	
evennum_list = list(filter(even_numbers,numbers))
print(numbers)
print(evennum_list)

 
	