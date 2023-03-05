
import sys

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def bubble(A, N):
    for i in range(0, N):
        print(i)
        print(A[i].value)
        for j in range(N-1, i-1, -1):
            if A[j].value < A[j - 1].value:
                A[j].value, A[j-1].value = A[j-1].value, A[j].value 
                A[j].suit, A[j-1].suit = A[j-1].suit, A[j].suit 

def selection(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
        A[i].value, A[minj].value = A[minj].value, A[i].value
        A[i].suit, A[minj].suit = A[minj].suit, A[i].suit

def isStable(C1, C2, N):
    for i in range(0, N):
        if C1[i].suit != C2[i].suit:
            return False
    return True

############ main ############
N = int(input())
i = 0
x = 0
C1=C2=[Card(0,0)]*N

X = input().split()

for x in X:
    x2 = list(x)
    print(x2)
    C2[i].suit = C1[i].suit = x2[0]
    C2[i].value = C1[i].value = int(x2[1])
    sys.stdout.write(str(C1[i].value))
    sys.stdout.write(C1[i].suit)
    i += 1

bubble(C1, N)
selection(C2, N)

print(N)
for c1 in C1:
    sys.stdout.write(c1.suit)
    sys.stdout.write(str(c1.value))
    sys.stdout.write(" ")

sys.stdout.write("\n")
sys.stdout.write("Stable")
sys.stdout.write("\n")

for c2 in C2:
    sys.stdout.write(c2.suit)
    sys.stdout.write(str(c2.value))
    sys.stdout.write(" ")

sys.stdout.write("\n")
if isStable(C1, C2, N):
    sys.stdout.write("Stable")
else:
    sys.stdout.write("Not Stable")
sys.stdout.write("\n")