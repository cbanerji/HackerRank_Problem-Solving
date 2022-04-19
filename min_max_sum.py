#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    dat = [sum(arr)-arr[-1]] # smallest
    dat.append (sum(arr)-arr[0]) #largest
    dat = " ".join(map(str, dat))
    print(dat)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
