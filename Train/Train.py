# 서울 지하철 2호선 스탬프 투어
# 서울 지하철 2호선 순환 부분에는 모두 43개의 역
# 일방통행으로만 갈 수 있다.
# 스탬프는 모든 역에서 찍을 수 있다.
# 2호선의 모든 역에는 1~43까지의 숫자가 붙어 있다고 가정
# 1번째 역에서 입장해서 17번째 역에서 나온다고 할 때,
# 스탬프를 찍는 순서에 몇 가지 패턴이 있을지 구하시오.

# 1
N = 43
start = 1
end = 17

def nCr(n, r):
  result = 1
  for i in range(1, r + 1):
    result = result * (n - i + 1) / i

  return result

def solution(N):
  cnt = 1
  for i in range(1, end):
    cnt += nCr(end - start - 1, i)
  for i in range(1, N - end + 1):
    cnt += nCr(N - end, i)

  return cnt

print(solution(N))

# 2
N = 43
start = 1
end = 17

station_count = abs(start - end)
print((1 << (station_count - 1)) + (1 << (N - station_count - 1)) - 1)