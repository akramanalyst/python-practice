import csv

file = open("example.csv","a+" ,newline="")
data = [
    ['rollno' , 'name', 'age' , 'city','course'],
    [1003,'Raja',20,'Lucknow','Diploma'],
    [1005,'wasim',25,'kolkata','BCA'],
    [12005, 'Himanshu Dogne' , 'Delhi','Egineering']

]
writer = csv.writer(file)
writer.writerows(data)
file.seek(0)
data = csv.reader(file)
for row in data:
    print(row)
file.close()
