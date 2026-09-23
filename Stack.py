n = int(input())

stack = []
result = []
num = 1

possible = True

for i in range(n):
    target = int(input())

    # target까지 스택에 넣기
    while num <= target:
        stack.append(num)
        result.append("+")
        num += 1

    # 스택의 가장 위 숫자가 target인지 확인
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