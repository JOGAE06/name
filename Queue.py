N = int(input())

a = []

for i in range(1, N + 1):
    a.append(i)

while len(a) > 1:
    a.pop(0)
    x = a.pop(0)
    a.append(x)

print(a[0])