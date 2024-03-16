def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Enter a non-negative number"))
if n<0:
    print("invalid input")
else:
    print("Fibonacci number at position ",n,"is ",fibonacci(n))
    
