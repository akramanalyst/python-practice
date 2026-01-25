#name = " atul kumar"
#for c in name:
#	print(c)

string = input(" enter a string ")
#v = [ 'a','e','i','o','u']
vowels= {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0 }
#vowels{ }
for c in string:
	if c in vowels:

	#if c in v:
		#if c in vowels:
			vowels[c]=vowels[c]+1
		#else:
			#vowels[c]=1
for k,v,in vowels.items():
	print(k,"=",v)