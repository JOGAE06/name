N = int(input())
A = list(map(int, input().split()))

stack = []
answer = [-1] * N

for i in range(N):

    while stack and A[stack[-1]] < A[i]:
        index = stack.pop()
        answer[index] = A[i]

    stack.append(i)

print(*answer)