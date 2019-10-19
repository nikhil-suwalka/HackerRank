#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
# def circularArrayRotation(a, k, queries):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k, q = [int(x) for x in input().split()]

    arr = [int(x) for x in input().split()]

    
    if(k>n):
        first = n-(k % n)    
    else:
        first = n-k
    for i in range(q):
        inp = int(input())
        if ((inp + first) < n):
            fptr.write(str(arr[inp + first]))
        else:
            fptr.write(str(arr[(inp+first)-n]))
        fptr.write('\n')    

    fptr.close()
