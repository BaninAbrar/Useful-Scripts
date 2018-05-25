# -*- coding: utf-8 -*-
"""
Created on Wed May  9 08:37:29 2018

@author: co-op1
"""

import math
    
def letter_counting(i):
    lettering = ''
    k = []
    kp = -1
    if i < 26:
        lettering = chr(i%26+65)
        return lettering

    n = int(math.log(i,26))
    if n >= 1:
        for l in range(0, n+1):
            kp += 26**(l)
            k.append(kp)
    for j in range(0, len(k)):
        if i < k[j]:
            continue
        index = (i-k[j])/26**j
        index = int(index)
        lettering = chr((index)%26+65) + lettering
    return lettering
    
if __name__ == "__main__":
    for i in range(0, 710):
        print(letter_counting(i))
