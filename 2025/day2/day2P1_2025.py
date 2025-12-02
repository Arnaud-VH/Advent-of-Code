def read_input():
   return [tuple(r.split("-")) for r in input().split(",")]

def solve():
   intervals = read_input()
   #We need the ID to be of even length, split in half and check if left is same as right
   sum = 0
   for interval in intervals:
      for i in range(int(interval[0]), int(interval[1])+1):
         length = len(str(i))
         if length % 2 != 0:
            continue
         if str(i)[:length//2] == str(i)[length//2:]:
           sum += int(i)
   return sum

print(solve())