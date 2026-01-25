#program to find the square of numbers in list using map.
'''
numbers = [2,3,4,9,8,7,5]
def squarefun(n) :
    return n ** 2
square_Num = list(map(squarefun,numbers))
print(square_Num)
'''
average = lambda x,y,z : (x+y+z)/3
print(average(4,6,8))

def average(x,y,z):
    return (x+y+z) / 3
print(average(3,5,4))
