#Write a Python program to triple all numbers in a given list of integers. Use Python map.
mylist = []
for i in range(10):
    num = int(input("Enter the elements of list : "))
    mylist.append(num)
print(mylist)
print("    ")
def fun(num):
    return num **3
triple_of_numbers = list(map(fun,mylist))
print(triple_of_numbers)

# 2nd method to find triple (cube) of numbers.
cube = list(map(lambda x : x ** 3,mylist))
print(cube)