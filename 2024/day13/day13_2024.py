import re
import numpy as np
NEW = 10000000000000
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

def solve(add=0):
   cost = 0
   for system in machines:
      a = [system[0][0],system[1][0]]
      b = [system[0][1],system[1][1]]
      if add != 0:
         y = [system[2][0]+add, system[2][1]+add]
         x = np.linalg.solve([a,b],y)
         nums = [round(num) for num in x if all(round(num) > 0 and abs(num-round(num)) < 0.001 for num in x)]
      else:
         x = np.linalg.solve([a,b],system[2])
         nums = [round(num) for num in x if all(round(num) <= 100 and round(num) > 0 and abs(num-round(num)) < 0.001 for num in x)]
      if nums:
         cost += 3*nums[0] + nums[1]

   return cost

readInput()
print(f"Part 1: " + str(solve()))
print(f"Part 2: " + str(solve(NEW)))
