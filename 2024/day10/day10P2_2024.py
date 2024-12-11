def readInput():
   with open('in.txt', 'r') as file:
      data = file.read()
   return [list(map(int, line)) for line in data.strip().split("\n")]

def distinctTrails(x,y,val,grid,seen):
   if (val==9):
      return 1
   seen[x][y] = True
   xDir = [0,1,0,-1]
   yDir = [-1,0,1,0]
   num = 0
   for i in range(len(xDir)):
      dx = x + xDir[i]
      dy = y + yDir[i]
      if (inBound(dx,dy,grid) and grid[dx][dy] == val+1 and not seen[dx][dy]):
         num += distinctTrails(dx,dy,val+1,grid,seen)
      
   seen[x][y] = False
   return num

def inBound(x,y,grid):
   return (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]))

def solve():
   grid = readInput()
   val = 0
   for row in range(len(grid)):
      for col in range(len(grid[0])):
         if (grid[row][col] == 0):
            seen = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
            val += distinctTrails(row,col,0,grid,seen)
   return val

print(solve())