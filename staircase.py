#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spc = " "
    chc = "#"
    for i in range (n,0,-1):
        print((i-1)*spc + (n-i+1)*chc)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
