import json
import requests

url = 'http://159.89.89.46:5000/nodes/resolve'

response = requests.get(url)
print(response)
