# python program to filter odd numbers from list.
# num = int(input("Enter the number of elements of list."))
#for i in range(1,num+1):
#print(mylst) 
mylist = []
num = int(input("Enter number of elements to add in list :  "))
for i in range(num):
    n = int(input("Enter elements to list : "))
    mylist.append(n)
print(mylist)
odd_numbers = list(filter(lambda x : x % 2!=0,mylist ))
print("odd_numbers from the above list :  " , odd_numbers)
print(sorted(mylist))
print(sorted(odd_numbers))
print("    ")

mylist.insert(i,n)
print(mylist)
print("   ")
mylist.remove(9)
print(mylist)

print("  ")
mylist.pop(4)
print(mylist)

print("    ")
mylist.pop()
print(mylist)
