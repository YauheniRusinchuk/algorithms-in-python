def insert_sort(A):
    ''' Сортировка списка вставками '''
    N = len(A)
    for top in range(1,N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

if __name__ == '__main__':
    pass
