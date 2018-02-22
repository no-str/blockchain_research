import json
import requests

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-i', '--ip', default='127.0.0.1', type=str, help='IP address of my node.')
parser.add_argument('-p', '--port', default=5001, type=int, help='Port my node will listen on.')

args = parser.parse_args()
ip = args.ip
port = args.port

node = 'http://' + ip + ':' + str(port)

transaction = {"nodes": [node]}
url = 'http://159.89.89.46:5000/nodes/register'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)

reply = response.json()

print('Node registration received.\n'+ reply['message'])
