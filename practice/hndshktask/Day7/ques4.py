import csv
file = open("example.csv","r")
data = file.readlines()
for row in data:
    print(row)
file.close()