import json
import requests

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-i', '--ip', default='127.0.0.1', type=str, help='IP address of my node.')
parser.add_argument('-p', '--port', default=5001, type=int, help='Port my node will listen on.')

args = parser.parse_args()
ip = args.ip
port = args.port

url = ('http://' + ip + ':' + str(port) + '/mine')

response = requests.get(url)

reply = response.json()

print(reply['message'])
