# python program to take coordinatesof a point as input and determine its quadrant.
--
x = int(input("Enter the value of x = "))
y= int(input("Enter the value of y = "))

if x == 0 and y == 0:
	print(" The point is at origin ")
elif x == 0:
	print(" The point lies on the Y-axis ")
elif y == 0:
	print(" The point lies on the X-axis ")
elif x > 0 and y > 0:
	print(" The point is in 1st quadrant ")
elif x < 0 and y > 0:
	print(" The point is in 2nd quadrant ")
elif x < 0 and y < 0:
	print(" The point is in 3rd quadrant ")
else : #x > 0 and y < 0
	print(" The point is in 4th quadrant ")

