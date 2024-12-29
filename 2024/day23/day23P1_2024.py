from collections import defaultdict

graph = defaultdict(set)
def readInput():
   with open("in.txt", "r") as file:
      data = file.read()
      for line in data.strip().split("\n"):
         u,v = line.split("-")
         graph[u].add(v)
         graph[v].add(u)
         
readInput()

def findTriples():
   triples = set()
   for vertex in graph:
      for n1 in graph[vertex]:
         for n2 in graph[vertex]:
            if n1 != n2 and n2 in graph[n1]:
               triple = [vertex,n1,n2]
               triple.sort()
               triples.add(tuple(triple))

   return triples

def solve():
   allTripels = findTriples()
   count = sum(any(node[0] == 't' for node in triple) for triple in allTripels)
   print(count)

solve()