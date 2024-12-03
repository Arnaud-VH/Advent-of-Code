import re

def readInput():
   with open("in.txt", "r") as file:
      lines = file.readlines()
      return ''.join(lines)

def solveMul():
   allInput = readInput()
   val = 0
   allTuples = re.findall(r'mul\(\d+\,\d+\)', allInput)
   for tp in allTuples:
      found = re.findall(r'\d+', tp)
      val += (int(found[0]) * int(found[1]))
   return val
      
print(solveMul())