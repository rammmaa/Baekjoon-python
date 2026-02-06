import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def solve(x, y, size):
    first_color = grid[x][y]
    is_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != first_color:
                is_same = False
                break
        if not is_same: break

    if is_same:
        return (1, 0) if first_color == 0 else (0, 1)

    half = size // 2
    
    res1 = solve(x, y, half)
    res2 = solve(x, y + half, half)
    res3 = solve(x + half, y, half)
    res4 = solve(x + half, y + half, half)

    total_white = res1[0] + res2[0] + res3[0] + res4[0]
    total_blue = res1[1] + res2[1] + res3[1] + res4[1]
    
    return (total_white, total_blue)

white_ans, blue_ans = solve(0, 0, n)

print(white_ans)
print(blue_ans)