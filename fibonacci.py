def fibonacci(n):
    if (n > 1):
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    else: 
        return n
    
n = int(input("Enter a numer:"))
print(fibonacci(n))
