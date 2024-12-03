def readInput():
   file = open("./in.txt")
   allReports = [[int(num) for num in line.split()] for line in file]
   return allReports

def checkReports():
   allReports = readInput()
   count = 0
   for report in allReports:
      increasing = all(((i < j) and abs(i-j) >= 1 and (abs(i-j) <= 3)) for i,j in zip(report, report[1:]))
      decreasing = all(((i > j) and abs(i-j) >= 1 and (abs(i-j) <= 3)) for i,j in zip(report, report[1:]))
      if (increasing or decreasing):
         count += 1

   return count

validReports = checkReports()
print(validReports)