#!/bin/python

import sys

n = int(raw_input().strip())

def powerof2(n):
    power = 0
    while n / 2**power >= 1:
        power += 1
    return power

def binary(n, power):
    binarystr = ""
    exponent = power-1
    while exponent >= 0:
        if n % 2**exponent == n:
            binarystr += "0"
            exponent -= 1
        else:
            binarystr += "1"
            n = n - 2**exponent
            exponent -= 1
    return binarystr

def consOnes(bnstr):
    count = 0
    maxCount = 0
    for letter in bnstr:
        if letter == "1":
            count += 1
        else:
            maxCount = max(count, maxCount)
            count = 0
    if count > maxCount:
        maxCount = count
    return maxCount
    
print consOnes(binary(n, powerof2(n)))