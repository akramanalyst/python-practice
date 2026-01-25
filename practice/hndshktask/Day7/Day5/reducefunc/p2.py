# program to find sum of all eleents in the list.
import functools
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
def sum_num(a,b):
    return a+b
total_sum = functools.reduce(sum_num,numbers)
print(total_sum)
'''
n = int(input("Enter value of n : "))
numbers = []
for i in range(1,n):
   
    numbers.append(i)
print(numbers)
def sum_of_num(a,b):
      return a+b
total_sum = functools.reduce(sum_of_num,numbers)
print(total_sum)
print("sum of numebrs from the generated list using lambda and reduce function :")
total_sum = functools.reduce(lambda a,b : a+b,numbers)
print(total_sum)
print("using sum()function : ")
print(sum(numbers))
print(pow(numbers))
print(type(numbers))

