def read_input():
   lines = []
   while True:
      try:
         lines.append(list(input().strip().split()))
      except EOFError:
         break
   return lines

def solve():
   lines = read_input()
   ops = lines[len(lines)-1]
   result = 0
   for col in range(len(lines[0])):
      cur = 0
      if ops[col] == "*":
         cur = 1
         for row in range(len(lines)-1):
            cur *= int(lines[row][col])
      else:
         cur = 0
         for row in range(len(lines)-1):
            cur += int(lines[row][col])

      result += cur
   return result
print(solve())