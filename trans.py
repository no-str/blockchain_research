import json
import requests

from argparse import ArgumentParser

from random import randint

parser = ArgumentParser()

parser.add_argument('-r', '--recip', default='127.0.0.1', type=str, help='IP address of the recipient.')
parser.add_argument('-p', '--port', default=5001, type=int, help='Port recipient listens on.')

args = parser.parse_args()
recip = args.recip
port = args.port

def new_bin(self):
    """
    Creates a random 4-digit bin number (bin_num)
    """
    range_start = 10**3
    range_end = (10**4)-1
    return randint(range_start, range_end)

#Generate a random bin number.
bin_num = new_bin(self)

transaction = {"sender": "Scott", "recipient": "Digi Node",
         "bin_num": str(bin_num)}
url = ('http://' + recip + ':' + str(port) + '/transactions/new')
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=transaction)

reply = response.json()

print('Transaction received.\n'+ reply['message'])
