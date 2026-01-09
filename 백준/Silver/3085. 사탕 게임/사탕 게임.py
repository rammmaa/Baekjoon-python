N = int(input())

candy = [list(input()) for _ in range(N)]

def check():
    max_len = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
                max_len = max(max_len, cnt)
            else:
                cnt = 1
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if candy[i][j] == candy[i-1][j]:
                cnt += 1
                max_len = max(max_len, cnt)
            else:
                cnt = 1
    return max_len

answer = 0

for i in range(N):
    for j in range(N-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]  # 교환
        answer = max(answer, check())
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]  # 복구

for i in range(N-1):
    for j in range(N):
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]  # 교환
        answer = max(answer, check())
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]  # 복구

print(answer)