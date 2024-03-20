'''
 You are given a list marks that has the marks scored by a class of students in a Mathematics test.
 Find the median marks and store it in a float variable named median. You can assume that marks is a list of float values.

Procedure to find the median

(1) Sort the marks in ascending order. Do not try to use built-in methods.

(2) If the number of students is odd, then the median is the middle value in the sorted sequence.
If the number of students is even, then the median is the arithmetic mean of the two middle values in the sorted sequence.

You do not have to accept input from the console as it has already been provided to you. 
You do not have to print the output to the console. Input-Output is the responsibility of the auto-grader for this problem.
'''
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    marks.sort()
  
    n = len(marks)
    if n % 2 == 1:
        median = marks[n // 2]
    else:
        mid1 = marks[n // 2 - 1]
        mid2 = marks[n // 2]
        median = (mid1 + mid2) / 2

    median = float(median)
### Enter your solution above this line
    return median
marks_input = input()

# Extracting numeric values from the input string
marks = [float(mark.strip()) for mark in marks_input.split(',') if mark.strip().isdigit()]


result = solution(marks)
print(result)
