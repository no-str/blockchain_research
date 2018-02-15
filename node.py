from uuid import uuid4

# New node object
class Node(object):
    uid = ""
    ip = ""
    port = 0

    #Constructor for the node object
    def __init__(self, uid, ip, port):
        # Generate a globally unique address for this node
        # uid = str(uuid4()).replace('-', '')
        self.uid = uid
        self.ip = ip
        self.port = port
