def generation_nubmer(N:int,M:int, prefix=None):
    ''' Генерирует все чилса (с лидирующими незначащими нулями)
    в N - ричной системе счисления(N<10)
    длины M
    '''
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generation_nubmer(N, M-1, prefix)
        prefix.pop()


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
    else:
        gen_bin(M-1,prefix+"0")
        gen_bin(M-1,prefix+"1")



print(generation_nubmer(3,3))
