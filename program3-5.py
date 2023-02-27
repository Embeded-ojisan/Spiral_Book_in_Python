
import sys

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def bubble(C1, N):

def selection(C1, N):

############ main ############
N = int(input())
i = 0
x = 0
C1=C2=[Card(0,0)]*N

X = input().split()

for x in X:
    C2[i].value = C2[i].suit = C1[i].value = C1[i].suit = int(x)
    i += 1

bubble(C1, N)
selection(C2, N)

print(N)
for c1 in C1:
    sys.stdout.write(c1.suit, c1.value)

sys.stdout.write("\n")