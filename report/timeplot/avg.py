#!/usr/bin/python

import sys

nums = []

for line in sys.stdin:
    nums.append(float(line.rstrip('\n').split()[1]))

if len(nums)>0:
    print(sum(nums)/len(nums))
