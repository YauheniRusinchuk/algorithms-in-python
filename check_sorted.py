def check_sorted(A,ascending=True):
    ''' Проверка отсортированности за O(N) '''
    N = len(A)
    flag = True
    s = 2** int(ascending) - 1
    for i in range(0,N-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag

result =  check_sorted([1,5,3,4,2])
print(result)
