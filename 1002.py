import math


cases = int(input()) #num of testcases
results = list(0 for i in range(cases)) #input's' -> print's', should store inputs
for i in range(cases):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # possible at python3

    distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2,2))
    check1 = r1 + r2
    check2 = abs(r1 - r2)

    if distance == 0: results[i] = -1 if (r1==r2) else 0
    elif distance == check1: results[i] = 1
    elif (distance < check1) and (distance > check2): results[i] = 2
    elif distance > check1: results[i] = 0
    elif distance == check2: results[i] = 1
    else: results[i] = 0

for i in range(cases):
    print(results[i])