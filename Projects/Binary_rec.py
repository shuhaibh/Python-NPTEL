# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:44:52 2024

@author: shuha
"""

def binary_search(l,x,start,end):
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return binary_search(l, x, start, mid-1)
        else:
            return binary_search(l, x, mid+1, end)
        
l=[20,45,60,70,90]
x=int(input("Enter search key"))
Index=binary_search(l, x, 0, len(l)-1)
if Index==-1:
    print (x ," not found")
else:
    print(x," is founa at position ",index+1)
