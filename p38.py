# string 
#immutable
name = "Aman chaurasiya"
print(type(name))
name = 'virat kohli'

#slicing
lenght = len(name)
print(name[ : ])
print(name)

print(name[0:5])


#multiline string

poem = " twinkle twinkle little star\nhow i wonder what you are"
print(poem)

print('    ')
poem = """ twinkle twinkle ,little star
how i wonder what you are"""
print(poem)

#iteration 
print('   ')
player = "virat kohli"
for c in player:
	print(c)

rev = ""
for c in player:
	rev = c+rev
print(rev)
print('    ')
print(player[::-1])