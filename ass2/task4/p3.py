"""
python program to create list of ten numbers by taing input from user named AR ,and copy even list in EAR,
and odd numbers in list OAR.now display elements of EAR and OAR.

"""

num = int(input(" Enter a number : "))
AR = [ ]
EAR = [ ]
OAR = [ ] 
for i in range(0,num+1):
	elements = int(input(" Enter elements of list : "))
	AR.append(elements)
	print("AR = ",AR)

	
	if elements % 2  == 0:
		#print(" numbers are even:")
		EAR.append(elements)
		print("EAR = ",EAR)
	else:
		OAR.append(elements)		
		print(" OAR =  " , OAR)
print(" Even numbers : ", EAR)
print(" Odd numbers :", OAR)