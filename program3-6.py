import sys

cnt=0
G=[0]

def insertionSort(A, n, g):
    global cnt
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

    for i in reversed(range(0, len(G))):
        insertionSort(A, n, G[i])

############ main ############
n = int(input())
i = 0
x = 0
A=[0]*n

for i in range(0, n):
    A[i] = int(input()) 

shellSort(A, n)

sys.stdout.write(str(len(G))+"\n")

for i in reversed(range(0, len(G)-1)):
    sys.stdout.write(str(G[i]))
    if i > 0:
        sys.stdout.write(" ")
sys.stdout.write("\n")
sys.stdout.write(str(cnt)+"\n")

for i in range(0, n):
    sys.stdout.write(str(A[i])+"\n")


