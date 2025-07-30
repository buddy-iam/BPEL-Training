import random

class ProofOfBurn:
   def __init__(self):
      self.miners = {}
      self.burn_contributions={}
   
   def add_miner(self, miner_id, balance):
      self.miners[miner_id] = balance
      self.burn_contributions[miner_id] = 0

   def burn_tokens(self, miner_id, amount ):
      if self.miners.get(miner_id, 0) < amount:
         print(f"Miner {miner_id} has insufficient balance to burn {amount} tokens.")
         return False
      
      self.miners[miner_id] -= amount
      self.burn_contributions[miner_id] += amount
      print(f"Miner {miner_id} burned {amount} tokens. Total burned : {self.burn_contributions[miner_id]}")
      return True
   
   def select_miner(self):
      total_burned = sum(self.burn_contributions.values())
      if total_burned == 0:
         raise ValueError("Total burn contributions must be greater than zero to select a miner.")
      
      selection_point = random.uniform(0, total_burned)
      current_sum = 0

      for miner, burned in self.burn_contributions.items():
         current_sum+=burned
         if current_sum>=selection_point:
            return miner
      return None
   
   def reward_miner(self, miner_id, reward=10):
      if miner_id in self.miners:
         self.miners[miner_id] += reward
         print(f"Miner {miner_id} rewarded with {reward} tokens. New balance: {self.miners[miner_id]}")
         return True
      
   
pob_system = ProofOfBurn()

pob_system.add_miner("Miner_A", 100)
pob_system.add_miner("Miner_B", 80)
pob_system.add_miner("Miner_C", 60)

pob_system.burn_tokens("Miner_A", 30)
pob_system.burn_tokens("Miner_B", 20)
pob_system.burn_tokens("Miner_C", 10)

selected_miner = pob_system.select_miner()
print(f"\n Selected Miner for Block Creation: {selected_miner}")

pob_system.reward_miner(selected_miner, reward=15)

print(f"\n Final Miner Balances and Burn Contributions: ")
for miner, balance in pob_system.miners.items():
   print(f"{miner} - Balance: {balance}, Total Burned: {pob_system.burn_contributions[miner]}")