def pow(a,n:int):
    if n == 0:
        return 1
    elif n%2 == 1: #нечетные
        return pow(a,n-1) * a
    else:
        return pow(a**2, n//2)

print(pow(2,2))        
