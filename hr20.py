#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
numSwaps = 0
for i in xrange(n-1):
    for j in xrange(n-1):
        if a[j] > a[j+1]:
            x = a[j]
            a[j] = a[j+1]
            a[j+1] = x
            numSwaps += 1
    if numSwaps == 0:
        break

print "Array is sorted in %s swaps." % str(numSwaps)
print "First Element: " + str(a[0])
print "Last Element: " + str(a[n-1])