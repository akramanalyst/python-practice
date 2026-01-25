# Dictionary.....

#empty dictionary
dict1 = { }

dict1 = { 'one' : "first elements"}
print(dict1['one'])# to get values
print(dict1.get('six')) # to get values
 
# adding element in dictionary
dict1["two"] = "second elements" #to add single value
dict1.update({ 3 : 'third', 4: 'four'}) # to add multiple values
# with same key value update  old to new on  that key.. 
dict1['one'] = 'second elements'
print(dict1)

# traversing over a dictionary

for k in dict1:
	print(k,"=" , dict1[k])
for k,v in dict1.items():
	print(k,v)
for k in dict1.keys():
	print(k)
for v in dict1.values():
	print(v)
for item in dict1.items():
	rint(item)