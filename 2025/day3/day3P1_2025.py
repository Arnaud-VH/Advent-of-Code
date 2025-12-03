def read_input():
   lines = []
   while True:
      try:
         line = input()
         lines.append(line)
      except EOFError:
         break
   return lines

def solve():
   total = 0
   for line in read_input():
      total += charge(line) 
   return total


def charge(line):
   nums = [int(c) for c in line]
   first = max(nums)
   result = 0
   if nums.index(first) == len(nums) - 1:
      first = max(nums[:len(nums)-1])
      result = first * 10 + nums[len(nums)-1]
   else:
      index = nums.index(first)
      end = len(nums) - 1
      maxNum = -1
      while end > index:
         if nums[end] > maxNum:
            maxNum = nums[end]
         end -= 1
      result = first * 10 + maxNum
   return result

print(solve())