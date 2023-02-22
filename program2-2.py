
num_lines = int(input())
R = [0] * num_lines

i = 0
while i < num_lines:
    R[i] = int(input())
    i += 1
    
maxv = -2000000
minv = R[0]

i = 0
while i < num_lines:
    maxv = max(maxv, R[i] - minv)
    minv = min(minv, R[i])
    i += 1

print(maxv)