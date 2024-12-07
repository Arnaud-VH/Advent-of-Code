def readInput():
   file = open("in.txt")
   operators = []
   targets = []
   for line in file:
      split = line.strip().split(":")
      numbers = [int(num) for num in split[1].split()]
      operators.append(numbers)
      targets.append(int(split[0]))
   return (targets, operators)

def checkOperators(target, numbers, val):
   if (target == val and not numbers):
      return True
   elif numbers:
      concat = int(str(val) + str(numbers[0]))
      return (checkOperators(target, numbers[1:], val+numbers[0]) or 
      checkOperators(target, numbers[1:], val*numbers[0]) or
      checkOperators(target, numbers[1:], concat))
   return False



def solve():
   targets, numbers = readInput()
   val = 0
   for i in range(len(targets)):
      if (checkOperators(targets[i], numbers[i], 0)):
         val += targets[i]
   return val

print(solve())