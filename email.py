import requests
import json
res=requests.get('https://gorest.co.in/public/v1/comments')
#print(dir(res))
#print(res.content)
#print(res.text)
#op=open("output1.json","w")
#op.write(res.text)
content=res.content
response=json.loads(content)
#r_dict=res.json()
for i in response['data']:
    print(i['email'])


