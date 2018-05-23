import insert_sort
import select_sort
import bubble_sort

def test_sort(sort_algorithm):
    print('testcase #1',end='')
    A = [4,2,5,1,3,7,12,8,6,]
    sort_algorithm(A)
    print(A)

if __name__ == '__main__':
    #test_sort(insert_sort.insert_sort)
    #test_sort(select_sort.select_sort)
    test_sort(bubble_sort.bubble_sort)
