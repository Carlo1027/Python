import json

data = '''{
    "name" : "Carlo",
    "phone" : {
        "type" : "intl",
        "number" : "+51 961 775 503"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
