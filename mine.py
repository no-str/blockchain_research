import json
import requests

url = 'http://159.89.89.46:5000/mine'

response = requests.get(url)
print(response)
