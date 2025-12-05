def read_input():
   #Need to think about not saving the intervals as arrays. 
   ranges = []
   line = input()
   while (line != ""):
      start,end = map(int, line.split("-"))
      ranges.append((start, end))
      line = input()
   line = input()
   ingredients = []
   ingredients.append(int(line))
   while True:
      try:
         ingredients.append(int(input()))
      except EOFError:
         break
   return ranges, ingredients

def solve():
   ranges, ingredients = read_input()
   count = 0
   for ing in ingredients:
      for val in ranges:
         if val[0] <= ing and ing <= val[1]:
            count += 1
            break
   return count

print(solve()) 