'''
Taken from iamshardul

https://www.hackerrank.com/challenges/encryption/submissions/code/15000772

really interesting Pythonic code golfing.

Created on 31 Dec 2015

@author: chris
'''
import math
s = raw_input().strip()
sLength = len(s)
rows = int(math.ceil(math.sqrt(sLength)))

for i in range(rows):
    print s[i::rows],