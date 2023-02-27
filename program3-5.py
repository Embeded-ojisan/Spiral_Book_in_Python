
import sys

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

############ main ############
N = int(input())
i = 0
x = 0
members=[Card(0,0)]*N

X = input().split()

for x in X:
    members[i].value = members[i].suit = int(x)
    i += 1

sys.stdout.write("\n")