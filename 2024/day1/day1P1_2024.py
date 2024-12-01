def readInput():
   list1 = []
   list2 = []
   while True:
      try:
         line = input()
         split = line.split("   ")
         list1.append(int(split[0]))
         list2.append(int(split[1]))
      except EOFError:
         break
   return (list1, list2)

def solve():
   list1, list2 = readInput()
   list1.sort()
   list2.sort()
   sum = 0
   for i in range(len(list1)):
      diff = list1[i] - list2[i]
      if diff < 0:
         diff *= -1
      sum += diff
   return sum

print(solve())






