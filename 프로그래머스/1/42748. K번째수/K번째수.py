def solution(array, commands):
    answer = []
    for i, j, k in commands:
        t = array[i - 1:j]
        t.sort()
        answer.append(t[k - 1])
    return answer