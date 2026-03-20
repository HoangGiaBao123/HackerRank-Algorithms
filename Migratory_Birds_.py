import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    birds = []
    for item in arr:
        while (arr.count(item) <= 1) and (arr.count(item) != 0):
            arr.remove(item)
    maximum = 0
    for i in arr:
        if arr.count(i) > maximum:
            maximum = arr.count(i)
    for a in arr:
        if arr.count(a) >= maximum:
            birds.append(a)
    return min(birds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
