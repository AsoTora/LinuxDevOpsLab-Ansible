import json

class FilterModule(object):
    def filters(self):
        return { 'a_filter': a_filter }

def a_filter(input, find="Identity"):
    accounts = json.loads(json.dumps(input))
    for i in accounts:
        if i['name'] == find:
            return(i['id'])