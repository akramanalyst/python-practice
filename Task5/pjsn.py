import json
file = open("a.json","r")
data = json.load(file)
print(data)
for k ,v in data.items():
    print(f"{k}:{v}")
file.close()