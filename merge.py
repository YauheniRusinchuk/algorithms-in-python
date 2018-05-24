def merge_sort(A:list,B:list):
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


result = merge_sort([3,4,5,6], [1,2,3,4])

print(result)
