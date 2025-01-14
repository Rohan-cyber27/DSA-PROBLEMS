# Calculate the factorial of a number iterative

def factorial_all(n):
    if n<0:
        return False
    result=1
    for i in range(1,n+1):
        result =result*i          #result*=i     
        print(result)

    return result

print(factorial_all(5))


# Calculate the factorial of a number recursive

def factorial_recursive(n):
    if n<0:
        return False
    if n==0 or n==1:
        return 1
    
    return n*factorial_recursive(n-1)


print(factorial_recursive(10))

