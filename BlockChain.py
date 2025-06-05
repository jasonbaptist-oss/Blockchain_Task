import hashlib
import time
class Block:
    def __init__(self,index,data,previous_hash,nonce=0):
        self.index=index
        self.data=data
        self.timestamp=str(time.time())
        self.nonce=nonce
        self.previous_hash=previous_hash
        self.hash=self.compute_hash()
    def compute_hash(self):
        block_string=str(self.index)+self.timestamp+str(self.data)+self.previous_hash+str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()
    def proof_of_work(self,difficulty=2):
        prefix=difficulty*"0"
        while not self.hash.startswith(prefix):
             self.nonce+=1
             self.hash=self.compute_hash()


class BlockChain:
    def __init__(self):
        self.chain=[]
        self.create_initial_block()
        self.length_of_blockchain=len(self.chain)
    def create_initial_block(self):
        initial_block=Block(0,"Initial Block","0",0)
        initial_block.proof_of_work()
        self.chain.append(initial_block)
    def add_block(self,data):
        new_block=Block(self.length_of_blockchain,time.time(),self.chain[self.length_of_blockchain-1].hash)
        new_block.proof_of_work()
        self.chain.append(new_block)
        self.length_of_blockchain=len(self.chain)
    def is_valid(self):
        for i in range(self.length_of_blockchain):
            if self.chain[i].hash != self.chain[i].compute_hash():
                print(f"Invalid hash at block(compute){i}")
                print(self.chain[i].hash)
                print(self.chain[i].compute_hash())
                return False
            if i<self.length_of_blockchain-1:
                if self.chain[i+1].previous_hash!=self.chain[i].hash:
                    print(f"Invalid hash at block(prev){i+1}")
                    return False
        return True



# Example usage
blockchain = BlockChain()
blockchain.add_block("Alice sends 5 BTC to Bob")
blockchain.add_block("Bob sends 2 BTC to Charlie")
blockchain.add_block("Charlie sends 1 BTC to Dave")

# Print the blockchain
for block in blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Nonce: {block.nonce}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print("=" * 60)

# Check if the blockchain is valid
print("Is the blockchain valid?", blockchain.is_valid())