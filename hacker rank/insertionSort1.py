#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value_to_insert = arr[n - 1]
    hole_position = n - 1

    while hole_position > 0 and arr[hole_position - 1] > value_to_insert:
        # Shift elements to the right
        arr[hole_position] = arr[hole_position - 1]
        hole_position -= 1
        print(" ".join(map(str, arr)))

    # Place the stored value at the correct position
    arr[hole_position] = value_to_insert
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
