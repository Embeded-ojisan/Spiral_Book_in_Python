import sys

cnt=0
G=[0]

def insertionSort(A, n, g):
    for i in range(g, n):
        v = A[i]
        j = i - g
    while j >= 0 and A[j] > v:
        A[j + g] = A[j]
        j -= g
        cnt += 1
    A[j+g]=v

def shellSort(A, n):
    h=1
    while True:
        if h > n:
            break
        G.append(h)
        h = 3*h + 1

    for i in reversed(range(0, G.size())):
        insertionSort(A, n, G[i])

############ main ############
n = int(input())
i = 0
x = 0
A=[0]*N

X = input().split()

for x in X:
    x2 = list(x)
    A[i] = x2[0]
    i += 1

shellSort(A, n)

