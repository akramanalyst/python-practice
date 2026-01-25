'''
c = int(input(' enter celsius  :'))
f = int(input('enter fahrenhiet  : '))
def  ftoc(c):
	fren = (c*9/5)+32
	return fren
	print('  ')
def ctof(f):
	print('    ')
	cel = (f -32)*5/9
	return cel
print(ftoc(c))
print(ctof(f))
'''

def ftoc(f):
	cel = (f-32)*5/9	
	return  cel
def ctof(c):
	far = (c*9/5)+32
	return far
print(" enter 1 for cel \n enter 2 for far: ")
ch = input()
if ch =='1':
	c= eval(input('enter temp in cel ') )
	print('fahrenheit = ',ctof(c))
elif ch=='2':
	f = eval(input('enter temp in fahrenheit: '))
	print('celsius = ',ftoc(f))
else:
	print('invaid choice:')