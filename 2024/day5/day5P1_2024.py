def readInput():
   allTuples = []
   count = 0
   while True:
      line = input()
      if (line == ""):
         break
      (x,y) = line.split("|")
      allTuples.append((x,y))

   allQueue= []
   while True:
      try:
         line = input()
         queue = line.split(",")
         allQueue.append(queue)
      except EOFError:
         break   

   return (allTuples, allQueue)

def getOrder(num, queue, allTuples):
   before = []
   after = []
   for pair in allTuples:
      if (num == pair[0] and pair[1] in queue):
         after.append(pair[1])
      elif (num == pair[1] and pair[0] in queue):
         before.append(pair[0])
   return (before,after)


def checkQueue(queue, allTuples):
   for num in queue:
      before, after = getOrder(num, queue, allTuples)
      numIndex = queue.index(num)
      #Check if first number cannot be first
      if (numIndex == 0 and before):
         return False
      for num2 in queue:
         checkIndex = queue.index(num2)
         if (numIndex < checkIndex and queue[checkIndex] in before):
            return False
         elif (numIndex > checkIndex and queue[checkIndex] in after):
            return False
   
   return True

def calcSum(validQueues):
   val = 0
   for queue in validQueues:
      index = len(queue)//2
      val += int(queue[index])
   return val

def solve():
   allInput = readInput()
   allTuples = allInput[0]
   allQueue = allInput[1]
   valid = []
   for queue in allQueue:
      if (checkQueue(queue, allTuples)):
         valid.append(queue)

   return calcSum(valid)

print(solve())