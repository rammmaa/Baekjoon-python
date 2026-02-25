x, y = map(int, input().split())
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

s = 0

for i in range(x - 1):
    s += m[i]

s += y - 1

print(d[s % 7])