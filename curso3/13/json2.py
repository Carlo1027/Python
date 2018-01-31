import json

data = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Carlo"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "André"
    }
]'''

info = json.loads(data)
print('User Count:',len(info))
for item in info:
    print('Name:',item['name'])
    print('Id:',item['id'])
    print('Attribute:',item['x'])
