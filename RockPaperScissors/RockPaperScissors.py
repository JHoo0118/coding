# 한 번에 결정하는 다수결 "가위 바위 보"
# 낼 수 있는 손은 '바위', '가위', '보' 중의 하나
# 이때 가장 많은 사람이 낸 손이 승리
# 예를 들어 6명이라면
# 바위 가위  보  결과
#    3   2   1  바위가 승리
#    1   4   1  가위가 승리
# 만약 4명의 경우, 한 번에 승자가 결정되는 조합은 12가지
# 100명의 사람이 있을 때, '한 번에 승리자가 결정될 수 있는 조합'은 몇 가지인가?

# 1
N = 100
cnt = 0

for r in range(N + 1):
  for p in range(N - r + 1):
    s = N - r - p
    maxValue = max(s, r, p)
    if maxValue == s and s > r and s > p:
      cnt += 1
    elif maxValue == r and r > s and r > p:
      cnt += 1
    elif maxValue == p and p > r and p > s:
      cnt += 1

print(cnt)

# 2
N = 100
cnt = 0
for r in range(N + 1):
  for p in range(N - r + 1):
    s = N - r - p
    all = [r, p , s]
    if all.count(max(all)) == 1:
      cnt += 1

print(cnt)