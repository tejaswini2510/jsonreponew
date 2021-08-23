import requests
import json
res=requests.get('https://gorest.co.in/public/v1/users')
content=res.content
response=json.loads(content) 
for i in response['data']:
    if i['id']==12:
        print(i['user'])
