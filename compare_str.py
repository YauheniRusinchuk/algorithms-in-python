def compare(A:str,B:str):
    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if A[i] != B[i]:
            return False

    return True
