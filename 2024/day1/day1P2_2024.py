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

def findSimilarity():
   list1, list2 = readInput()
   list1.sort()
   list2.sort()
   similarity = 0
   index1 = 0
   index2 = 0
   while (index1 != 999 and index2 != 999):
      if (list1[index1] < list2[index2]):
         index1 += 1
      elif (list1[index1] > list2[index2]):
         index2 += 1
      else:
         count = 0
         while(list2[index2+count] == list1[index1]):
            count += 1
         index2 += count
         similarity = similarity + (list1[index1]*count)

   return similarity
   
print(findSimilarity())
