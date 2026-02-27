def solution(n):
    answer = 0
    s = sorted(str(n), reverse=True)
    answer = int(''.join(s))
    return answer