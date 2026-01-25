
#import random
#import randomas rn
from random import randint

#print(random.randint(1,10))
#print(rn.randint(1,10))
#print(randint(1,10))
#print(randint(1000,9999))


num = randint(1,10)
while True:

	guess = int(input(" guess the number b/w 1-10 : "))
	if num == guess:
		print(" you won ")
		break
	else:
		print("better luck nxt time")

 