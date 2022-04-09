#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    al = 0
    bo = 0
    sub = subt(a,b)
    for p in sub:
        if p > 0:
            al = al+1
        elif p <0:
            bo = bo+1
        else :
            pass

    return [al,bo]

def subt(a,b):
    diff = []
    zip_object = zip(a, b)
    for a, b in zip_object:
        diff.append(a-b)
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
