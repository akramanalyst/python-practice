'''
sentence = input("enter a line")
find_what = input("find what ??")
replace_with = input("replace with??")

new = sentence.replace(find_what,replace_with)
print(sentence)
print(new)


sent = "   the sun rises in the east  "
print(sent)
sent = sent.strip()#remove white space from starting and ending 
words  = sent.split(" ") #returns a list,based on the separator
print(sent)
print(words)

print("word count=",len(words))
print("character count=",len(sent))


ch = 0
ws = 0
for c in sent:
	if c.isspace():
		ws+=1
	else:
		ch+=1
print(ch,ws)

characters = []
for c in sent:
	#if not c.isspace():
		characters.append(c)
print(characters)



#join function

lst = ['riya','john','Alice','jonathan']
s = "+".join(lst)
print(s)
s=", ".join(lst)
print(type(s))
print(s)


name = input("enter name : ").lower()
print("palindrome" if name == name[::-1] else "not palindrome")
'''

n = int(input('enter number  : '))
print('binary = ' , bin(n)[2:])
print("octal = ",oct(n)[2:])
print("hexa = ",hex(n)[2:])