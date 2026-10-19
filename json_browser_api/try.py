import json

x = {"name" : "john",
     "age" : 30,
     "city" : "New york" }

y = json.dumps(x)
print(x)
print(y)