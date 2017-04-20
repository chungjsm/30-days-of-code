#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

revarr = arr[::-1]

# hacky solution...
string = ""

for e in revarr:
    string += str(e)
    string += " "

print string