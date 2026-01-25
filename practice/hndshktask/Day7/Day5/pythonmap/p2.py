#Write a Python program to add three given lists using Python map and lambda.
lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]
lst3 = [7,8,9,10,11]
'''
add_of_lists = list(map(lambda x,y,z : x+y+z , lst1,lst2,lst3 ))
print(add_of_lists)
'''
def sum_of_lists(x,y,z):
    return x+y+z
result = list(map(sum_of_lists,lst1,lst2,lst3))
print(result)