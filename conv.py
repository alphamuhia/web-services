import json

python_di = {"name": "peter", "age": 30, "class": "software eng"}

json_string = json.dumps(python_di)

print(python_di["name"])
print(python_di["age"])
print(python_di["class"])

print(json_string)

