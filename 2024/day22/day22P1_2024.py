import math
def readInput():
   secretNumbers = []
   with open("in.txt", "r") as file:
      data = file.read()
      for line in data.strip().split("\n"):
         secretNumbers.append(int(line))
   return secretNumbers

def mix(nowSecret, result):
   return nowSecret ^ result

def prune(nowSecret):
   return (nowSecret % 16777216)

def getNext(secret):
   result = secret*64
   result = mix(secret, result)
   newSecret = prune(result)
   result = math.floor(newSecret/32)
   result = mix(newSecret, result)
   newSecret = prune(result)
   result = newSecret*2048
   result = mix(newSecret, result)
   newSecret = prune(result)
   return newSecret

def finalSecret(start):
   newSecret = start
   for i in range(2000):
      newSecret = getNext(newSecret)
   
   return newSecret

def solve():
   secretNumbers = readInput()
   val = 0
   for number in secretNumbers:
      result = finalSecret(number)
      val += result
   print(val)

solve()