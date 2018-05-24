def merge(A:list,B:list):
    '''Сортировка слиянием
    Слияние отсортированных массивов
    '''
    C = [0] * (len(A) + len(B))
    i=k=n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]; i+=1;n+=1
        else:
            C[n] = B[k]; k+=1;n+=1

    while i<len(A):
        C[n] = A[i]; i+=1;n+=1

    while k<len(B):
        C[n] = B[k]; k+=1;n+=1

    return C


def merge_sort(A):
    print(A)
    if len(A) <= 1:
        return

    middle = len(A) // 2
    left = [A[i] for i in range(0,middle)]
    right = [A[i] for i in range(middle,len(A))]

    merge_sort(left)
    merge_sort(right)

    C = merge(left,right)
    for i in range(len(A)):
        A[i] = C[i]

    print(A)



merge_sort([3,4,5,1,2,3,4,5,11,2,3])
