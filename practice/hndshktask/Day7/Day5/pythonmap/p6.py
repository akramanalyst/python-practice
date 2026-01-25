#Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
def change_case(s):
    return str(s).upper(),str(s).lower()
chars = {'a','e','k','n','r','e','a'}
result = map(change_case,chars)
print(set(result))
print("    ")
names = ["akram","jamal","naeem","jamal"]
result = list(map(list,names))
print(result)