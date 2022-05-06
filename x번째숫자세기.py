# 알고리즘 잡스 CT 이벤트 문제
# < x번째 숫자 구하기 2 >
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

