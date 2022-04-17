#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    alti = []
    valley = 0
    for i in range (steps):
        if path[i] == 'D':
            altitude += -1
            alti.append(altitude)
        elif path[i] == 'U':
            altitude += 1
            alti.append(altitude)
        else:
            pass

        if i>0 and alti[i-1] < 0 and alti[i] == 0:
            valley += 1

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
