#Write a Python program to square the elements of a list using the map() function.
numbers = [2,3,4,5,6,7,8,9,10]
print(numbers)
# square of list using map and lambda.
#result = list(map(lambda x : x**2,numbers))
#print(result)
# square oflist using function and map
def square_of_list(n):
    return n ** 2
result = list(map(square_of_list,numbers))
print(result)