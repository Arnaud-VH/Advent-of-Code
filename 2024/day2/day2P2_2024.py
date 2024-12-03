from typing import Iterable

def readInput():
   file = open("./in.txt")
   allReports = [[int(num) for num in line.split()] for line in file]
   return allReports

def isSafe(report):
   increasing = all(((i < j) and abs(i-j) >= 1 and (abs(i-j) <= 3)) for i,j in zip(report, report[1:]))
   decreasing = all(((i > j) and abs(i-j) >= 1 and (abs(i-j) <= 3)) for i,j in zip(report, report[1:]))
   if (increasing or decreasing):
      return True
   
   return False

def skipReactor(report):
   for index in range(len(report)):
      yield report[:index] + report[index + 1:]

def checkWithBadReports():
   allReports = readInput()
   count = 0
   for report in allReports:
      if (isSafe(report)):
         count += 1
      elif(any(isSafe(skipped) for skipped in skipReactor(report))):
         count += 1
               
   return count

print(checkWithBadReports())
