
import sys

def selectionSort(A, N):
    sw=0

    for i in range(0,N-1):
        minj=i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
        if i != minj:
            sw+=1
    return sw


############ main ############
N = int(input())
A = [0] * 100
i = 0
x = 0

X = input().split()

for x in X:
    A[i] = int(x)
    i += 1

sw = selectionSort(A, N)

i=0
while i < N:
    if i > 0:
        sys.stdout.write(" ")
    sys.stdout.write(str(A[i]))
    i+=1

sys.stdout.write("\n")
sys.stdout.write(str(sw))
sys.stdout.write("\n")
