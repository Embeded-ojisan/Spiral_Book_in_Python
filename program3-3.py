
import sys

def bubbleSort(A, N):
    sw = 0
    flag = True
    i = 0
    while flag == True:
        flag = False
        j = N-1
        while j >= i + 1:
            if A[j] < A[j -1]:
                A[j-1], A[j] = A[j], A[j-1]
                flag=True
                sw+=1
            j-=1
        i+=1
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

sw = bubbleSort(A, N)

i = 0
while i < N:
    if i:
        sys.stdout.write(" ")
    sys.stdout.write(str(A[i]))
    i+=1
sys.stdout.write("\n")
sys.stdout.write(str(sw))    
sys.stdout.write("\n")
