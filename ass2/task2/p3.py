#program to find roots of quadratic equation ax2+bx+c=0.

import math
#import cmath #use for complex math
a=int(input("enter coefficient of x^2 = "))
b=int(input("enter coefficient of x = "))
c=int(input("enter the constant = "))
#d=b**2-4*a*c
#if d<0
	#print("roots are imaginary ")
#else:
root1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
root2 = (-b+math.sqrt(b*b-4*a*c))/(2*a)

#root1 = (-b+cmath.sqrt(b*b-4*a*c))/(2*a)
#root2 = (-b-cmath.sqrt(b*b-4*a*c))/(2*a) 
print("root1= ",root1)
print("root2=",root2)
