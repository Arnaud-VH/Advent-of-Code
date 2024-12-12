nums = [int(num) for num in input().split(" ")]

dpStones = {}

def splitStones(stone, iterations):
   if (iterations == 0):
      return 1
   if (stone, iterations) in dpStones:
      return dpStones[(stone,iterations)]
   if (stone == 0):
      dpStones[(stone,iterations)] = splitStones(1, iterations-1)
   elif len(str(stone)) % 2 == 0:
      middle = len(str(stone))//2
      strNum = str(stone)
      left = int(str(stone)[:middle])
      right = int(str(stone)[middle:])
      dpStones[(stone,iterations)] = splitStones(left, iterations-1) + splitStones(right, iterations-1)
   else:
      dpStones[(stone,iterations)] = splitStones((stone*2024), iterations-1)
   
   return dpStones[(stone,iterations)]

val = 0
for stone in nums:
   val += splitStones(stone, 75)

print(val)