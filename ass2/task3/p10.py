# python program to create random() function.this fucntion retunr random number from 1-10.
import random
a = [ 1,2,3,4,5,6,7,8,9,10 ]
def random():
	return random.choice(a)
print(random())