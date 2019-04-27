import json

def OpenJson(name):
    with open('%s.json' % name , 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    return data

def SaveJson(name, data):
    with open('%s.json' % name , 'w') as f:
                json.dump(data, f)