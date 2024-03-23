import json
with open('./info.json') as f:
    infos = json.loads(f.read())
print(infos['mysql_id'])
print(infos['mysql_pass'])