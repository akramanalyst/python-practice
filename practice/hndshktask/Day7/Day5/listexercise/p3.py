#program to calculate sum and average of all numbers of list.
from functools import reduce
numbers = [10,20,30,40,50]
# sum of numbers using for loops.
summ = 0
for i in numbers:
    summ = summ+i
print(summ)  
average = summ/5
print(average)

print(" ")
#sum of numbers using sum() function.
summation = sum(numbers)
avg = summation/len(numbers)
print(summation)
print(avg)
print("   ")
# summation of numbers using lambda function.
total_sum = reduce(lambda x,y : x+y,numbers)
print(total_sum)

def sum_of_numbers(num):
    num = 0
    for i in numbers:
        num = num + i
    return num
total_sum = list(map(sum_of_numbers,numbers))
print(total_sum) 