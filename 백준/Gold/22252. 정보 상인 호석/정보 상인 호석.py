import heapq

Q = int(input())
mp = {}
ans = 0

for _ in range(Q):
    s = input().split()
    t = int(s[0])
    name = s[1]

    if t == 1:
        k = int(s[2])
        h = mp.get(name)
        if h is None:
            h = []
            mp[name] = h
        for i in range(3, 3 + k):
            heapq.heappush(h, -int(s[i]))
    else:
        b = int(s[2])
        h = mp.get(name)
        if not h:
            continue
        for _ in range(b):
            if not h:
                break
            ans -= heapq.heappop(h)
print(ans)