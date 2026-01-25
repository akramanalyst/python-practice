cd #take full name as input and print short name.

fullname = input("enter full name : ").title()

words = fullname.split(" ")
print(words)
shortname = ""
for n in words[0:len(words)-1]:
	shortname = shortname+n[0]+". "

shortname = shortname+words[-1]
print(shortname)