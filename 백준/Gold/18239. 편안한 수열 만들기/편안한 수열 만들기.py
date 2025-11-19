import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    # N = 3만 불가능
    if N == 3:
        print("NO")
        return

    print("YES")

    # N = 2 (K는 무조건 1)
    if N == 2:
        # swap 1 2를 5번
        for _ in range(5):
            print("swap 1 2")
        return

    # N >= 4 인 경우들

    # K = 1
    if K == 1:
        # swap 1 2
        print("swap 1 2")
        # reverse 2 N
        print(f"reverse 2 {N}")
        # reverse 2 N-1
        print(f"reverse 2 {N-1}")
        # reverse 1 N 두 번
        print(f"reverse 1 {N}")
        print(f"reverse 1 {N}")
        return

    # K = N-1
    if K == N - 1:
        # swap N-1 N
        print(f"swap {N-1} {N}")
        # reverse 1 N-1
        print(f"reverse 1 {N-1}")
        # reverse 2 N-1
        print(f"reverse 2 {N-1}")
        # reverse 1 N 두 번
        print(f"reverse 1 {N}")
        print(f"reverse 1 {N}")
        return

    # 일반 케이스: 2 <= K <= N-2
    # 3번의 reverse로 정렬 + 2번은 패딩
    print(f"reverse 1 {K}")
    print(f"reverse {K+1} {N}")
    print(f"reverse 1 {N}")
    print(f"reverse 1 {N}")
    print(f"reverse 1 {N}")

if __name__ == "__main__":
    main()
