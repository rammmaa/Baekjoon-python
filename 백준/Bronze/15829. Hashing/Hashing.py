l = int(input())
s = input()

sum = 0
for i in range(l):
    a = ord(s[i]) - ord('a') + 1
    sum += (a) * (31 ** i)
    
sum %= 1234567891
print(sum)