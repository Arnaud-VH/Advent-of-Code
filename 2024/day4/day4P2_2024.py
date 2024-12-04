def readInput():
   with open('in.txt', 'r') as file:
      grid = file.read().splitlines()
      
   return grid

def checkWord(grid, r, c):
   n = len(grid)
   m = len(grid[0])
   if (0 < r < n-1 and 0 < c < m-1):
      topLeft = grid[r-1][c-1]
      topRight = grid[r+1][c-1]
      bottomLeft = grid[r-1][c+1]
      bottomRight = grid[r+1][c+1]
      if (((topLeft == "M") or (bottomRight == "M")) and 
      ((topLeft == "S") or (bottomRight == "S")) and 
      ((topRight == "M") or (bottomLeft == "M")) and 
      ((topRight == "S") or (bottomLeft == "S"))):
         return True
      else:
         return False
   return False

def solveSearch():
   grid = readInput()
   count = 0
   directions = [(1,1),(1,-1),(-1,-1),(-1,1)]
   for r in range(len(grid)):
      for c in range(len(grid[0])):
         if (grid[r][c] == "A"):
            if (checkWord(grid, r, c)):
               count += 1
   return count

print(solveSearch())
