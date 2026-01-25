# python program to find series of prie number in given range .range must be enter as a input from user.
 
ll = int(input("enter the lower limit : "))
ul = int(input("enter the upper limit : "))
"""
for i in range(ll,ul+1):
	print(i)
i=ll
while i<=ul:
	print(i)
	i=i+1
"""	
import time
for n in range(ll,ul+1):
	c=0
	i=1
	while i<=n:
		if n%i==0:
			c=c+1
		i=i+1
	if c==2:
		print(n)
		time.sleep(1)
