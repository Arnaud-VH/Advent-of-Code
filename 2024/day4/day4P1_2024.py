def readInput():
   with open('in.txt', 'r') as file:
      grid = file.read().splitlines()
      
   return grid

def checkWord(grid, r, c, rDir, cDir):
   n = len(grid)
   m = len(grid[0])
   word = "XMAS"
   subString = ""
   while (0 <= r < n and 0 <= c < m and word.startswith(subString)):
      if (subString == word):
         return True
      else:
         subString = subString + grid[r][c]
         r += rDir
         c += cDir
         if (subString == word):
            return True
   
   return False

def solveSearch():
   grid = readInput()
   count = 0
   directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
   for r in range(len(grid)):
      for c in range(len(grid[0])):
         if (grid[r][c] == "X"):
            for rDir, cDir in directions:
               if (checkWord(grid, r, c, rDir, cDir)):
                  count += 1
   return count
   
print(solveSearch())