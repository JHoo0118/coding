# 직사각형을 정사각형으로 나누기
# 8 x 5의 직하각형 종이가 있을 때, 5 x 5의 정사각형으로 자르면 3 x 5의
# 직사각형이 남게 된다. 남은 3 x 5의 정사각형을 다시 3 x 3의 정사각형
# 으로 자르면 3 x 2의 직사각형이 남는다. 이를 2 x 2의 정사각형으로 자르면
# 1 x 2의 직사각형이 남으므로, 마지막으로 1 x 1의 정사각형 2개가 된다.
# 최종적으로 5개의 정사각형이 만들어진다. 긴 변의 길이가 1,000 이하에서
# 만들어질 수 있는 정사각형 개수가 딱 20개인 직사각형의 가로세로 길이 쌍이
# 몇 쌍인지 구하라. 이때 직사각형의 가로세로 길이를 바꾼 경우는 하나로 취급

w, n = 1000, 20

def divide(w, h):
    if w == h:
        return 1
    if h > w:
        w, h = h, w
    q, r = divmod(w, h)
    result = q
    if n - q < 0 or r == 0:
        return result
    else:
        result += divide(h, r)
    return result
        
cnt = 0
for i in range(1, w + 1):
    for j in range(i, w + 1):
        if divide(i, j) == n:
            cnt += 1
            
print(cnt)