import sys
input = sys.stdin.read

def solve():
    data = input().split()
    iterator = iter(data)
    
    N = int(next(iterator))
    M = int(next(iterator))
    
    parent = list(range(N + 1))
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        
        curr = x
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
            
        return root

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        
        if rootA != rootB:
            parent[rootB] = rootA

    for _ in range(M):
        u = int(next(iterator))
        v = int(next(iterator))
        union(u, v)
    
    first_lecture = int(next(iterator))
    current_root = find(first_lecture)
    
    ans = 0
    
    for _ in range(N - 1):
        next_lecture = int(next(iterator))
        next_root = find(next_lecture)
        
        if current_root != next_root:
            ans += 1
            current_root = next_root
            
    print(ans)

if __name__ == "__main__":
    solve()