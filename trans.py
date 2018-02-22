import json
import requests

transaction = {"sender": "Scott", "recipient": "Digi Node",
 "bin_num": "1234"}
url = 'http://159.89.89.46:5000/transactions/new'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)
print(response)
