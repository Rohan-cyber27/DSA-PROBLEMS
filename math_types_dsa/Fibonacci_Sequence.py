# Print the Fibonacci series up to N terms.

def fib_seriesR(n):
    if n <=0:
        print("please inter  the positve integer")
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    print(fib)

fib_seriesR(20)

# Print the Fibonacci series up to N terms.(itrative approch)

def fib_seriesI(n):
    if n <=0:
        print("enter positve number")
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    
    a,b=0,1
    result=[0,1]
    for _ in range(2,n):
        a,b=b,a+b
        result.append(b)
    return result

print(fib_seriesI(20))

# Find the N-th Fibonacci Number (Recursive Approach)


def fibonacci_recursive(n):
    if n <=0:
        print("enter positve number")
    if n==1:
        return 0
    elif n==2:
        return 1
    
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

n = 10
print(f"The {n}-th Fibonacci number is: {fibonacci_recursive(n)}")


# Find the N-th Fibonacci Number (Itraative Approach)

def fib_seriesI(n):
    if n <=0:
        print("enter positve number")
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    
    a,b=0,1
    result=[0,1]
    for _ in range(2,n):
        a,b=b,a+b
        result.append(b)
        result1=result.pop()
    return result1

print(fib_seriesI(10))


