#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades, grades_count):
    # Write your code here
    for i in range (grades_count):
        if grades[i] < 38:
            pass
        elif grades[i] >= 38:
            num = grades[i]-(grades[i]%5) + 5
            if num-grades[i] <3:
                grades[i] = num
            else:
                pass
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades,grades_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
