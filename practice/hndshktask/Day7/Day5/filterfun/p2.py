mylist = [False,True,True,0,40,None]
print(list(filter(None,mylist)))

result = list(filter(None,mylist))
print(result)
print(type(result))