import csv 
file = open("myfile.csv", "r")
file.seek(0)
#data = file.readlines()
data = file.read()
#for row in data:
#   print(row)
print(data)
file.close()