#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    p = 0
    q = 0
    for i in range (n):
        p = p+arr[i][i]
        q = q+arr[i][n-i-1]
    diff = abs(p-q)

    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
