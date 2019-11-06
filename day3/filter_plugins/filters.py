class FilterModule(object):
    def filters(self):
        return {
            'account_id': account_id
        }

def account_id(arg, name="Identity"):
    import json
    accounts = json.loads(json.dumps(arg))

    for i in accounts:
        if i['name'] == name:
            return i['id']
