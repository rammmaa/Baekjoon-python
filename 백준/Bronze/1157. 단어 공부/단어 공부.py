word = input().upper()
cnt = [0] * 26

for c in word:
    cnt[ord(c) - ord('A')] += 1

max_cnt = max(cnt)

if cnt.count(max_cnt) > 1:
    print('?')
else:
    print(chr(cnt.index(max_cnt) + ord('A')))
