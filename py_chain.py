import hashlib, datetime

class PyBlock:
    def __init__(self, idx, timestamp, data, prev_hash):
        self.idx = idx
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.block_hash = self.hash_block()

    def get_index(self):
        return self.idx

    def get_block_hash(self):
        return self.block_hash

    def hash_block(self):
        block_hash = hashlib.sha256()
        block_hash.update((str(self.idx) +
                           str(self.timestamp) +
                           str(self.data) +
                           str(self.prev_hash)).encode('utf-8'))
        return block_hash.hexdigest()

    def __repr__(self):
        return 'Block index = {}\nBlock hash = {}\n'.format(self.get_index(),
                                                            self.get_block_hash())


def generate_first_block():
    '''
    Generate the first block in the chain with index = 0
    and the string '0' as previous hash.
    '''
    return PyBlock(0, datetime.datetime.now(), 'first_block', '0')


def build_block(previous_block):
    '''
    Take the last built block as parameter and
    build the next one
    '''
    index = previous_block.get_index() + 1
    data = 'not the first, but the number ' + str(index)
    prev_hash = previous_block.get_block_hash()

    return PyBlock(index, datetime.datetime.now(), data, prev_hash)

## Test ##
chain = [generate_first_block()]
first_block = chain[0]

chain.append(build_block(first_block))

for block in chain:
    print(block)
