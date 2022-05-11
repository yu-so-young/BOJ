# https://ssafylive.org/SSAFY_CT_EV 

x = int(input())
sequence = ""
i = 0
bit = 0

while(bit <= x):
    i += 1
    sequence += str(2*i)
    bit += len(str(2*i))

print(sequence[x-1])

