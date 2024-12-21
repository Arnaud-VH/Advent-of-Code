def readInput():
   coords = []
   with open("in.txt", "r") as file:
      data = file.read()
      for line in data.strip().split("\n"):
         (x,y) = line.split(",")
         coords.append((int(x),int(y)))
   return coords[:1024]

def inBound(x,y):
   return (x >= 0 and x < 71 and y >= 0 and y < 71)

def BFS(startx, starty, coords):
    queue = [(startx, starty)]
    distances = {(startx, starty): 0}
    while len(queue) > 0:
        x, y = queue.pop(0)
        for newX, newY in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if inBound(newX, newY) and (newX,newY) not in coords:
                coord = newX, newY
                if coord not in distances:
                    distances[coord] = distances[x, y] + 1
                    queue.append(coord)
    return distances

def solve():
   coords = readInput()
   val = BFS(0,0,coords)[(70,70)]
   return val

print(solve())
