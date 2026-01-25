# python program to take number of a days as input and display years , weeks and days.

n = int(input("Enter the number = "))
y = n//365
#w = (n-365)//7
w = n%365//7
d = n%365%7 
print("year = ",y)
print("weeks = ",w)
print("day = ",d)