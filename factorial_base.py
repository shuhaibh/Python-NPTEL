# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:58:14 2024

@author: shuha
"""

def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product

n=int(input("Enter a positive number:"))
if n<0:
    print("Factorial is not possible for negative numbers")
else:
    f=factorial(n)
    print("Factorial of ",n," is ",f)