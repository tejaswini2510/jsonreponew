import requests
import json
op=open("/home/deepcompute/Downloads/data.json","r")
for i in op:
    i=json.loads(i)
    print(datetime.datetime.fromtimestamp(i['dt_db_updated']).strftime('%Y-%m-%d %H:%M;%S'))


