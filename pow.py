import hashlib
import time
import matplotlib.pyplot as plt

class Block:
   def __init__ (self, index, previous_hash, timestamp, data, difficulty):
      self.index=index
      self.previous_hash=previous_hash
      self.timestamp=timestamp
      self.data=data
      self.difficulty=difficulty
      self.nonce=0
      self.hash=self.calculate_hash()

   def calculate_hash(self):
      block_string =f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
      return hashlib.sha256(block_string.encode()).hexdigest()
   
   def mine_block(self):
      target ='0'*self.difficulty
      while self.hash[:self.difficulty] != target:
         self.nonce+=1
         self.hash=self.calculate_hash()

      print(f"Block mined: {self.hash}")

class Blockchain:
   def __init__(self):
      self.chain=[self.create_genesis_block()]

   def create_genesis_block(self):
      return Block(0,"0",time.time(), "Genesis Block", difficulty=2)
   
   def get_latest_block(self):
      return self.chain[-1]
   
   def add_block(self, new_block):
      new_block.previous_hash=self.get_latest_block().hash
      new_block.mine_block()
      self.chain.append(new_block)

def main():
   difficulty_levels = [2,3,4,5,6,7]
   mining_times=[]

   for difficulty in difficulty_levels:
      blockchain =Blockchain()
      print(f"\nMining with difficulty level : {difficulty}")

      start_time = time.time()

      print("Mining Block 1....")
      block1 = Block(1, "", time.time(), "Block 1 Data", difficulty)
      blockchain.add_block(block1)

      print("Mining Block 2....")
      block2 = Block(2, "", time.time(), "Block 2 Data", difficulty)
      blockchain.add_block(block2)

      end_time = time.time()
      mining_times.append(end_time - start_time)

   plt.figure(figsize=(10,6))
   plt.plot(difficulty_levels, mining_times, marker='o')
   plt.title('Mining Time vs. Difficulty Level')
   plt.xlabel('Difficulty Level')
   plt.ylabel('Time(seconds)')
   plt.grid(True)
   plt.show()

if __name__ == "__main__":
   main()