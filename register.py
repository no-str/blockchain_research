import json
import requests

transaction = {"nodes": ["http://127.0.0.1:5000"]}
url = 'http://127.0.0.1:5000/nodes/register'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)
print(response)
