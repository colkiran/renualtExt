"""
load - load used to read the JSON data from a file
loads - used to convert json string to python dictionary
"""
import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)
for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("-" * 60)
# loads
empdata = '{"name": "Kevin", "age": 40, "desig": "MGR", "dept": "Finance", "salary": 150000}'
print(empdata)
print(type(empdata))

print("-" * 60)
edata = json.loads(empdata)
print(f"edata :{edata}")
print(type(edata))

print("-" * 60)
for k, v in edata.items():
    print(k, "=>" , v)
