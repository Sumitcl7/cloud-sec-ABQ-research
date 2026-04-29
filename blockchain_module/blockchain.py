import hashlib
import json
from time import time

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, data=None, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': data,
            'previous_hash': previous_hash or self.get_previous_block()['hash'],
        }

        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def add_data(self, data):
        prev_block = self.get_previous_block()
        return self.create_block(data, prev_block['hash'])

    def display_chain(self):
        for block in self.chain:
            print(block)