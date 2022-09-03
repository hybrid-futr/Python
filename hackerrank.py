#hackerrank: 0
#Given an array 'x' of integers 'n' calculate and print the respective mean, median, and mode on separate lines.
#If your array contains more than one modal value, choose the numerically smallest one.
import statistics

N = input()
A = [eval(i) for i in input().split(' ')]

print(statistics.mean(A))
print(statistics.median(A))
print(min(statistics.multimode(A)))