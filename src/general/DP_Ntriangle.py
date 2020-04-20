def solution(triangle):
    answer = 0
    tmp = list()
    for i in range(0, len(triangle)):
        if i == 0:
            tmp.append(triangle[i])
            continue

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))