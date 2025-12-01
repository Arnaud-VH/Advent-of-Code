def read_input():
   lines = []
   while True:
      try:
         line = input()
         lines.append((line[0],line[1:]))
      except EOFError:
         break
   return lines

def solve():
   pairs = read_input()
   start = 50
   count = 0
   for pair in pairs:
      if pair[0] == 'L':
         start -= (int(pair[1]) % 100)
         if start < 0:
            start = 100 + start
      else:
         start += (int(pair[1]) % 100)
         if start > 99:
            start = start - 100
      if start == 0:
         count += 1

   return count 

print(solve())