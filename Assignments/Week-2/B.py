'''
Accept three positive integers as input and check if they form the sides of a right triangle.
Print YES if they form one, and NO if they do not. The input will have three lines, with one integer on each line.
The output should be a single line containing one of these two strings: YES or NO.
'''
A = int(input())
B = int(input())
C = int(input())

if (A * A) + (B * B) == (C * C):
    print("YES",end="")
if (A * A) + (B * B) != (C * C):
    print("NO",end="")
'''
(correct solution)
'''
A = int(input())
B = int(input())
C = int(input())

if (A * A) + (B * B) == (C * C):
    print("YES",end="")
if (A * A) + (B * B) != (C * C):
    print("NO",end="")
