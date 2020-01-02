# def solution(n):
#     answer = []
#     return answer

n = 4
answer = [0]


def solution(n):
    if n == 1:
        return answer
    for _ in range(1, n):
        answer.append(0)
        for j in range(len(answer) - 2, -1, -1):
            if answer[j] == 0:
                answer.append(1)
            elif answer[j] == 1:
                answer.append(0)
    return answer


print(solution(n))
