def readInput():
   with open('in.txt', 'r') as file:
      data = file.read()
   return [list(map(int, line)) for line in data.strip().split("\n")]

def findTrails(x, y, val, grid, foundPoints):
   if (val == 9):
      foundPoints.add((x,y))    
   else:
      xDir = [0,1,0,-1]
      yDir = [-1,0,1,0]

      for i in range(len(xDir)):
         dx = x + xDir[i]
         dy = y + yDir[i]
         if (inBound(dx,dy,grid) and grid[dx][dy] == val+1):
            findTrails(dx, dy, val+1, grid, foundPoints)

def inBound(x,y,grid):
   return (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]))

def solve():
   grid = readInput()
   val = 0
   for row in range(len(grid)):
      for col in range(len(grid[0])):
         if (grid[row][col] == 0):
            foundPoints = set()
            findTrails(row,col,0,grid,foundPoints)
            val += len(foundPoints)

   return val

print(solve())