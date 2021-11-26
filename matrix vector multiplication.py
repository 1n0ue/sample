n,m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]
for i in range(n):
    answer = 0
    for j in range(m):
        answer += A[i][j]*b[j]
    print(answer)