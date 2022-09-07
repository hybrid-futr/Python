#hackerrank: 0
#Given an array 'x' of integers 'n' calculate and print the respective mean, median, and mode on separate lines.
#If your array contains more than one modal value, choose the numerically smallest one.
import statistics

N = input()
A = [eval(i) for i in input().split(' ')]

print(statistics.mean(A))
print(statistics.median(A))
print(min(statistics.multimode(A)))

#hackerrank: 0+1
#Given an array X of N integers and an array W representing the respective weights of X's elements,
#calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    #code goes here

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)