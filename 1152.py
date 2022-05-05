#1152 B2 단어 개수 세기

# 1 하나씩 체크
sentence = input()
count, check = 0, 1 #count 단어개수 check 이전이 스페이스라면 1, 문자라면 0
for i in range(len(sentence)):
    if (sentence[i] != " "): #문자고
        count += check
        check = 0
    else: check = 1
print(count)

# 2 method 사용
s = input().strip() # 양쪽 공백 삭제
print(s.count(' ') + 1 if s else 0) # 공백 개수 세기