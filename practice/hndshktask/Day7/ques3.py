# create and read the .txt file.
file = open("example.txt","a+")
file.write("\n hi this is Akram and he is a data Analyst")
file.seek(0)
data = file.read()
print(data)
'''
for row in data:
    print(row)
    '''
file.close()
