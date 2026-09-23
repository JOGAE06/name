n = int(input())

stack = []
result = []
num = 1

possible = True

for i in range(n):
    target = int(input())
    
    while num <= target:
        stack.append(num)
        result.append("+")
        num += 1

    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        possible = False

if possible:
    for x in result:
        print(x)
else:
    print("NO")
