'''
n = 10
people = [i for i in range(n, 0, -1)]
print(people)

result = ['1', '2', '3']

print("<", ", ".join(result) ,">", sep='')
'''

a = [1, 2, 3]
b = []
b.append(a.pop(2))
print(b)