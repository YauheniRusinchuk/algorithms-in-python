def select_sort(A):
    '''Сортировка выбором '''
    N = len(A)
    for pos in range(0,N-1):
        for k in range(pos+1,N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k] 


if __name__ == '__main__':
    pass
