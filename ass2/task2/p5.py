# python program to compute gross salary .

bsal = int(input(" Enter the basic salary = "))
if bsal <= 4000 :
	hra = bsal*10/100
	da = bsal*50/100
elif bsal > 4000 and bsal < 8000 :
	hra = bsal*15/100
	da = bsal*60/100
elif bsal > 8000 and bsal < 12000 :
	hra = bsal*20/100
	da = bsal*70/100
elif bsal > 12000:
	hra = bsal*25/100
	da = bsal*80/100
#else : 
gsal = bsal+hra+da
print(" Total gross salary = ", gsal)
