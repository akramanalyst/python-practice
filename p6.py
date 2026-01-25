# python program to calculate electricity bill.

u= int(input("enter unit consums = "))

if u<=150:
	bill = u*2.4
	print("total bill = ", bill)
elif u>150 and u<=300:
	bill = 150*2.4+(u-150)*3.00
	print("total bill = ", bill)
else:
	bill = 150*2.4+150*3.0+(u-300)*3.2
	print("total bill = ", bill)