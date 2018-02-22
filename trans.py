import json
import requests

transaction = {"sender": "Port 5000", "recipient": "someone else's address",
 "bin_num": "6789"}
url = 'http://127.0.0.1:5000/transactions/new'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)
print(response)
