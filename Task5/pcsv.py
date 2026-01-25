import csv
'''
file = open("a.csv","r")
data = file.readlines()
print(data)
print( "     "  )

for row in data:
    print(row)

file.close()
'''
file =open("a.csv","a+",newline="")
data = [
    ["RollNo","Name","course"],
    ["1027","Hanshika","Diploma"],
    ["1028","suyash","B.tech"],
    ["1004","Akram","B,tech"]

]

writer = csv.writer(file)
writer.writerows(data)

file.seek(0)
data = csv.reader(file)
for row in data:
    print(row)
file.close()

