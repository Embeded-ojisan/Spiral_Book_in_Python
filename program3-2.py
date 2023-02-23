
def trace(A, N):
    i = 0
    while i < N:
        if i > 0:
            print(" ")
        print(A[i])
        i+=1
    print("\n")

def insertionSort(A, N):
    i = 1
    j = 0
    v = 0

    while i < N:
        v = A[i]
        j = i - 1
        while j >= 0 & A[j] > v:
            A[j + 1] = A[j]
            j-=1
        A[j + 1] = v
        trace(A, N)

############ main ############

N = int(input())
A = [0] * N
i = 0
x = 0

X = input().split()

for x in X:
    A[i] = int(x)
    i += 1

trace(A, N)
insertionSort(A, N)