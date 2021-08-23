import requests
import json
op=open("/home/deepcompute/Downloads/demo.json","r")
for i in op:
    i=json.loads(i)
    print(i['total_count'])


