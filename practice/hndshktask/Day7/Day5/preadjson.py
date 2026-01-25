import json

file = open("myfile.json", "r")
data = json.load(file)
print(data["users"][0])
# for k,v in data.items():
#     print(f"{k}:{v}")

file.close()