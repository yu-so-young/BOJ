# 1065, silver4, 한수
# 결국 본질적으로 한수는 등차수열인게 중요해, 각 자리의 차이만 일정하게 유지되면 count

def isHansu(num):
    numlist = list(map(int,str(num)))
    if n <= 99:
        return 1

    for i in range(len(numlist)-2):
        if (numlist[i]-numlist[i+1] != numlist[i+1]-numlist[i+2]):
            return 0

    return 1


n = int(input())
count = 0
for i in range(n):
    count += isHansu(i+1)

print(count)
