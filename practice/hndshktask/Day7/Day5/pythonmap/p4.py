#Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
numbers = [10,30,15,20,50,60]
index = [1,2,3,4,5,6]
print(numbers)
print(index)
result = list(map(pow,numbers,index))
print(result)