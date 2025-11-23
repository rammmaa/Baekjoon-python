N = int(input())
x = []

for _ in range(N):
    x.append(list(map(int,input().split(' '))))
x.append(x[0])

answer = 0
for i in range(N):
    answer += x[i][0]*x[i+1][1] - x[i+1][0]*x[i][1]

print(abs(answer)/2)