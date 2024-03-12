#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c=Counter(ar)
    s=set(ar)
    c1=0
  #  print(c)
   # print(s)
    for v in s:
        v1=c.get(v)
        if v1%2==0:
            c1+=v1
        elif v1>2:
            print(v1,c1)
            c1+=v1-1
     #       print('......')
    #        print(c1)
    return c1//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
