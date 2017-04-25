#!/bin/python

import sys

def hourglass(arr, x, y):
    hgSum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] +arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
    return hgSum

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

maxSum = hourglass(arr, 0, 0)

for x in range(0,4):
    for y in range(0,4):
        if hourglass(arr, x, y) > maxSum:
            maxSum = hourglass(arr, x, y)
            
print maxSum