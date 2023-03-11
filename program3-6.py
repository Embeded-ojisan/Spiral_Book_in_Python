import sys

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

