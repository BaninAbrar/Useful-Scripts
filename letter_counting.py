# -*- coding: utf-8 -*-
"""
Created on Wed May  9 08:37:29 2018

@author: co-op1
"""

import math

#for i in range(100):
#    lettering = ''
#    for j in range(0,int(i/26)):
#        if j % 2 == 0:
#            lettering = lettering + chr(j%26+65)
#        else:
#            lettering = chr(j%26+65) + lettering
#    lettering += chr(i%26+65)
#    print(lettering)

#for i in range(0,720):
#    lettering = ''
#    if i < 25:
#        lettering += chr(i%26+65)
#        print(lettering)
#    else:
#        o = 0
#        if i != 26 and int(i/(676+26)) < 0:
#            for j in range(0, int(math.log(i,26))):
#                o += 26**j #* (int(math.log(i,26)) + 1)
#        for j in range(0, int(math.log(i-o,26))): # get number of letters
#            k = int(i/26**(j+1)) - 1
#            lettering = chr(k%26+65) + lettering
#        lettering += chr(i%26+65)
##        print('i is: ' + chr(i%26+65))
#        print(lettering)
#k = -1
#for j in range(0,3):
#    k += 26**j


for i in range(0, 73):
    lettering = ''
    kp = 0
    k = []
    n2 = 0
    if i < 26:
        lettering += chr(i%26+65)
        print(lettering)
    else:
        n = int(math.log(i, 26))
        for j in range(0, n):
            kp += 26**(j+1)
            if i >= kp:
                k.append(kp)
        for j in range(0, len(k)):
            n2 = int(math.log(k[j], 26))
            o = int(i/k[j]) - 1
            lettering = chr(o%26+65) + lettering
        lettering += chr(i%26+65)
        print(lettering)
#    print(k)
