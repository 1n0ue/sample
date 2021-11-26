r,c = map(int,input().split())
A = [list(map(int,input().split())) for i in range(r)]
answer = 0
row_sum = 0 #行和
column_sum = 0 #列和
for i in range(r):
    for j in range(c):
        answer += A[i][j]
        row_sum += A[i][j]
        print(answer,end=' ')
        answer = 0
    print(row_sum)
    row_sum = 0

lastrow_sum = 0
last_sum = 0
for i in range(c):
    for j in range(r):
        lastrow_sum += A[j][i]
        last_sum += A[j][i]
    print(lastrow_sum,end=' ')
    lastrow_sum = 0
print(last_sum)