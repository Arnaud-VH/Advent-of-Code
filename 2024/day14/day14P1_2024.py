import re
def readInput():
   robots = []
   with open('in.txt', 'r') as file:
      data = file.read()
      for line in data.strip().split("\n"):
         A = re.findall(r'-?\d+', line)
         robot = [(int(A[0]),int(A[1])),(int(A[2]),int(A[3]))]
         robots.append(robot)
   return robots

def finalPosition(start, vector):
   newX = (start[0] + 100*vector[0]) % 101
   newY = (start[1] + 100*vector[1]) % 103
   return (newX, newY)

def findQuadrant(x,y):
   if (x < 101 // 2 and y < 103 // 2):
      return 0
   elif (x > 101 // 2 and y < 103 // 2):
      return 1
   elif (x < 101 // 2 and y > 103 // 2):
      return 2
   else:
      return 3

def solve():
   robots = readInput()
   finals = [0]*4
   for robot in robots:
      finalPos = finalPosition(robot[0], robot[1])
      if (finalPos[0] != 101 // 2 and finalPos[1] != 103 // 2):
         finals[findQuadrant(finalPos[0], finalPos[1])] += 1
   val = 1
   print(finals)
   for entry in finals:
      val *= entry
   return val
      
print(solve())