# program to perform list manipulation.
mylist = [10,20,30,40,50]
print(mylist)
print(len(mylist))
# adding 600 at last position in list. 
mylist.append(600)
print(mylist)
print(len(mylist))
#inserting 300 at second index in the list.
mylist.insert(2,300)
print(mylist)
print(len(mylist))
#removing last element from the list
mylist.pop()
print(mylist)
print(len(mylist))
#removing element from the 0 index to the list.
mylist.pop(0)
print(mylist)
print(len(mylist))
mylist.remove(300)
print(mylist)
print(len(mylist))