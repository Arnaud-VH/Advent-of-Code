def readInput():
   with open('in.txt', 'r') as file:
      data = file.read()
   
   return [list(line) for line in data.strip().split("\n")]

def startDirPos(grid):
   count = 0
   for row in grid:
      if "^" in row:
         return ((0,-1), (row.index("^"), count))
      count += 1

def updateDirection(x,y):
   if ((x,y) == (0,-1)):
      return (1,0)
   elif((x,y) == (1,0)):
      return (0,1)
   elif((x,y) == (0,1)):
      return (-1,0)
   else:
      return (0,-1)

def solve():
   grid = readInput()
   direction, startCoords = startDirPos(grid)
   coords = [0]*2
   coords[0] = startCoords[0]
   coords[1] = startCoords[1]
   unmarked = [[0] * (len(grid[0])) for i in range(len(grid))]
   unmarked[coords[1]][coords[0]] = "X"
   while (0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])):
      if (grid[coords[1]][coords[0]] == "#"):
         coords[0] -= direction[0]
         coords[1] -= direction[1]
         x,y = updateDirection(direction[0], direction[1])
         direction = (x,y)
         unmarked[coords[1]][coords[0]] = "X"
         coords[0] += direction[0]
         coords[1] += direction[1]
      else:
         unmarked[coords[1]][coords[0]] = "X"
         coords[0] += direction[0]
         coords[1] += direction[1]

   count = 0
   for i in range(len(unmarked)):
      for j in range(len(unmarked[0])):
         if (unmarked[i][j] == "X"):
            count += 1

   return count         

   
print(solve())