# 1. Iterative Approach to Check if a Number is Prime
def check_prime(n):
    if n <=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


n= 29

print(check_prime(n))

# Print All Prime Numbers Up to N (Iterative)

def check_prime1(n):
    if n <=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

def all_prime(n):
    prime=[]
    for  i in range(2,n+1):
        if check_prime1(i):
            prime.append(i)
    return prime

print(all_prime(50))




