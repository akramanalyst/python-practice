# wap to store empid , empname,and salary in a file
file = open('emp.txt','a+')
file.write("\n10002\n rahim\n 50000")
file.seek(0)
data = file.read()
print(data)
file.close()