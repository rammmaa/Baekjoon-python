import sys

def main():
    E, S, M = map(int, sys.stdin.readline().split())
    y = 1
    while True:
        if (y - 1) % 15 + 1 == E and (y - 1) % 28 + 1 == S and (y - 1) % 19 + 1 == M:
            print(y)
            return
        y += 1

if __name__ == "__main__":
    main()
