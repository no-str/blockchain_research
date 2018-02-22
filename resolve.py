import json
import requests

url = 'http://127.0.0.1:5000/nodes/resolve'

response = requests.get(url)
print(response)
