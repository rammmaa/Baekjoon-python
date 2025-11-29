import sys
input = sys.stdin.readline


u, v = map(int, input().split())
A = input().rstrip()
B = input().rstrip()
N = len(A)
if N >= 22:
    if u > v:
        print("ras")
    elif u < v:
        print("auq")
    else:
        if A > B:
            print("ras")
        elif A < B:
            print("auq")
        else:
            print("rasauq")
else:
    a = int(A, u)
    b = int(B, v)
    if a > b:
        print("ras")
    elif b > a:
        print("auq")
    else:
        print("rasauq")