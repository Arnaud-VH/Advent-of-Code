import re

def readInput():
   with open("in.txt", "r") as file:
      lines = file.readlines()
      return ''.join(lines)

def solveDoAndDont():
   allInput = readInput()
   val = 0
   allFound = re.findall(r'mul\(\d+\,\d+\)|do\(\)|don\'t\(\)', allInput)
   flag = True
   for found in allFound:
      numbers = re.findall(r'\d+', found)
      if (not numbers):
         checkEnable = re.findall(r'don', found)
         if (checkEnable):
            flag = False
         else:
            flag = True
      if (flag and numbers):
         val += (int(numbers[0]) * int(numbers[1]))
         
   return val
print(solveDoAndDont())