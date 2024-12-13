import re
import numpy as np
machines = []
def readInput():
   with open('in.txt', 'r') as file:
      data = file.read()
      temp = []
      count = 0
      for line in data.strip().split("\n"):
         if line:
            A = re.findall(r'\d+', line)
            A = [int(num) for num in A]
            temp.append(A)
            count += 1
            if (count == 3):
               machines.append((temp[0],temp[1],temp[2]))
               count = 0
               temp = []

def solve():
   cost = 0
   for system in machines:
      a = [system[0][0],system[1][0]]
      b = [system[0][1],system[1][1]]
      x = np.linalg.solve([a,b],system[2])
      nums = [round(num) for num in x if all(round(num) <= 100 and round(num) > 0 and abs(num-round(num)) < 0.001 for num in x)]
      if nums:
         cost += 3*nums[0] + nums[1]

   return cost
readInput()
print(solve())
