import json
data = {
    "roolno" : "1028",
    "name": "suyash",
    "course":"B.Tech",
    "branch": "cse",
    "year":"4th year",
    "city":"Ayodhya"
    }
file = open("student.json","w")
json.dump(data,file,indent = 4)
file.close()