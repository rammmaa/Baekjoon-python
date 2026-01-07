import sys

for line in sys.stdin:
    n = int(line)
    remainder = 1 % n
    count = 1
    
    while remainder != 0:
        remainder = (remainder * 10 + 1) % n
        count += 1
    
    print(count)