# python program to calculate electricity bill based on the given parameters.

unit = int(input(" Enter the unit consumes : "))
if unit <= 150:
	bill = unit*2.4
elif unit > 150 and unit < 300:
	bill = 150*2.4+(unit-150)*3.0
elif unit > 300:
	bill = 150*2.4+(unit-150)*3.0+(unit-300)*3.2
print(" Total bill = ", bill)