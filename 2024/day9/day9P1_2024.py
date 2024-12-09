allInput = input()
count = 0
numFiles = 0
nums = []
for character in allInput:
   if (count % 2 == 0):
      for i in range(int(character)):
         numFiles += 1
         nums.append(count//2)
   else:
      if (int(character) != 0):
         for i in range(int(character)):
            nums.append(-1)
   count += 1

leftIndex = 0
rightIndex = len(nums)-1
while (leftIndex < rightIndex):
   while (nums[leftIndex] != -1 and leftIndex < rightIndex):
      leftIndex += 1
   while (nums[rightIndex] == -1 and rightIndex > leftIndex):
      rightIndex = rightIndex - 1
   if (leftIndex < rightIndex):
      nums[leftIndex] = nums[rightIndex]
      leftIndex += 1
      rightIndex -= 1

print(sum([number * i for i, number in enumerate(nums[:numFiles])]))
