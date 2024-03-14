# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:39:34 2024

@author: shuha
"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("Enter a positive number:"))
if n<0:
    print("Factorial is not possible for negative numbers")
else:
    f=factorial(n)
    print("Factorial of ",n," is ",f)