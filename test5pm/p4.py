'''
wap to create a list by user input.now display list 
elements in ascending and descending order.
''' 
num = int(input("enter the list elements:"))
mylst = []
for i in range(num):
	mylst.append(i)
	print(mylst)
print("ascending order:")
print(sorted(mylst))
print("descending order:")
print(mylst[::-1])

