def solution(brown, red):
    w = 3
    answer = []
    while True:
        for h in range(3, w + 1):
            if brown == w * 2 + (h - 2) * 2 and red == (w - 2) * (h - 2):
                answer.append(w)
                answer.append(h)
                return answer
        w += 1


brown, red = 24, 24

print(solution(brown, red))
