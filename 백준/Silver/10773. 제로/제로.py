import sys

it = iter(sys.stdin.read().split())
k = int(next(it))
st = []

for _ in range(k):
    x = int(next(it))
    if x == 0:
        st.pop()
    else:
        st.append(x)

print(sum(st))
