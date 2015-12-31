'''
Solving the "Encryption" hackerrank puzzle.

https://www.hackerrank.com/challenges/encryption

Not really encryption.

-----------------------------

Problem Statement

An English text needs to be encrypted using the following encryption scheme. 
First, the spaces are removed from the text. Let L be the length of this text. 
Then, characters are written into a grid, whose rows and columns have the following constraints:

floor(sqrt(L))<=rows<=column<=ceil(sqrt(L)), where |_x_| is floor function and |-x-| is ceil function
For example, the sentence if man was meant to stay on the ground god would have given us roots after removing spaces is 54 characters long, so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots
Ensure that rowsxcolumns>=L
If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rowsxcolumns.
The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message in English with no spaces between the words. The maximum message length can be 81 characters. Print the encoded message.

-----------------------------

Obviously inefficient data access pattern. But I think this is part
of the problem.

Created on 31 Dec 2015

@author: chris
'''
import math

s = raw_input().strip()

rows = int(math.floor(math.sqrt(len(s))))
columns = int(math.ceil(math.sqrt(len(s))))
if rows*columns < s:
    rows += 1

op = []
for i in range(columns):
    for j in range(rows):
        ind = i+j*columns
        if ind < len(s):
            op.append(s[ind])
    
    op.append(' ')

print ''.join(op)[:-1]
