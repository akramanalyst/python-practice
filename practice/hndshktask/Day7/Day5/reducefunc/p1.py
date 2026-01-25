# program to find max number from the given list.
import functools
numbers = [10,2,4,5,7,15,20,25]
def max1(x,y):
    if x > y:
        return x
    else : 
        return y
max_numbers = functools.reduce(max1,numbers)
print(max_numbers)
