#text = .txt
#csv = .csv
#json = .json
# text file 
# syntax 
#file = open("file_name","mode")

file = open("emp.txt","a+")
file.write("\n Hello , this is wriiten by python . ")
file.seek(0)
data = file.read()
print(data)
file.close()