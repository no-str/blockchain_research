import json
import requests

transaction = {"nodes": ["http://180.150.12.207:5000"]}
url = 'http://159.89.89.46:5000/nodes/register'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)
print(response)
