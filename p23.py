"""
# to check value present in dictionary on not.
dict2 = {
        1 : 'one' ,
        2 : 'two'
}
if  2 in dict2:
	print("present")
else:
	pritn("not present")

"""

#num = int(input(" enter 5 number : "))
dict1 = { }

for i in range(5):
	k = (input("enter key :" ))
	v = (input(" enter value: "))
	dict1[k] = v
print(dict1)