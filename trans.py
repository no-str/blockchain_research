import json
import requests

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-r', '--recip', default='127.0.0.1', type=str, help='IP address of the recipient.')
parser.add_argument('-p', '--port', default=5001, type=int, help='Port recipient listens on.')

args = parser.parse_args()
recip = args.recip
port = args.port

transaction = {"sender": "Scott", "recipient": "Digi Node",
 "bin_num": "1234"}
url = ('http://' + recip + ':' + str(port) + '/transactions/new')
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)
print(response)
