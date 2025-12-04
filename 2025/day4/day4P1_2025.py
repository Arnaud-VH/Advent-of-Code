def read_input():
   grid = []
   while True:
      try:
         line = list(input())
         grid.append(line)
      except EOFError:
         break
   return grid


def solve():
   grid = read_input()
   xDir = [-1,-1,0,1,1,1,0,-1]
   yDir = [0,1,1,1,0,-1,-1,-1]
   count = 0
   for r in range(len(grid)):
      for c in range(len(grid[0])):
         rollCount = 0
         if grid[r][c] == "@":
            for i in range(len(xDir)):
               dx = r + xDir[i]
               dy = c + yDir[i]
               if in_bound(dx,dy,grid) and grid[dx][dy] == "@":
                  rollCount += 1
            if rollCount < 4:
               count += 1
   return count         

def in_bound(x,y, grid):
   return (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]))

print(solve())