import csv
'''
file = open("myfile2.csv","w")
data = file.write("hello !  this is python code\n which is executed on vs code tools"  )
file.seek(0)
data = file.read()
print(data)
file.close()
'''
file = open("myfile2.csv", 'a+',newline="")
data = [
    ['rollno' , 'name' , 'age' , 'course', 'department'],
    [13004 , 'Rohit', 22,'B.tech','IT'],
    [13005, 'Sachin', 23 ,  'B.tech','CSE'],
    [13006 , 'Umaira', 23 , 'Diploma','civil']
]
w = csv.writer(file)
w.writerows(data)
file.seek(0)
data = csv.reader(file)
for row in data:
    print(row)
file.close()