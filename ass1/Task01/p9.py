# python program to find out simple interest.

p = int(input("Enter the principle value = "))
n = int(input("Enter the time period = "))
r = int(input("Enter the rate of interest = "))

si = (p*n*r)/100
print("simple interest = ",si)
print(type(si))