N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)] 

def solve(x, y, size):
    if size == 1:
        return grid[x][y]
    
    half = size // 2

    p = [
        solve(x, y, half),
        solve(x + half, y, half),
        solve(x, y + half, half),
        solve(x + half, y + half, half)
    ]

    p.sort()
    return p[1]

print(solve(0, 0, N))