import requests
import json
res = requests.get('https://gorest.co.in/public/v1/users')
content=res.content
res1=json.loads(content)
for i in res1['data']:
    print(i['name'])
    print(i['email'])


