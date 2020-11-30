# Квадратичные сортировки O(N**2)
## 1 Insert Sort
def insert_sort(A):
    """ Сортировка списка А вставками """
    N = len(A)
    for top in range(1,N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k-=1

## 2 Choise Sort
def choice_sort(A):
    """ Cортировка списка А выбором """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

## 3 Bubble Sort
def bubble_sort(A):
    """ Cортировка списка А методом пузырька """
    N = len(A)
    for bypass in range(1,N):
        for k in range(0,N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1],A[k]

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algorithm(A)
    print("Test passed!" if A == A_sorted else "Test Fail!") ## Тернарный оператор

    print("testcase #2: ", end="")
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Test passed!" if A == A_sorted else "Test Fail!")

    print("testcase #3: ", end="")
    A = [4,2,4,2,1]
    A_sorted = [1,2,2,4,4]
    sort_algorithm(A)
    print("Test passed!" if A == A_sorted else "Test Fail!")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)