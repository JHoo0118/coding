# 로마 숫자 변환 규칙
# 아라비아 숫자와 로마 숫자 대응표
# 아라비아 숫자  1  5  10  50  100  500  1,000
#     로마 숫자  I  V  X   L    C    D     M
# 예를들어 27이라면 10 + 10 + 5 + 1 + 1 로
# 표현할 수 있으므로, 'XXVII'라고 표기
# 4를 'IIII', 9를 'VIIII'라고 적을 수 없음
# 4는 'IV', 9면 'IX'
# 로마 숫자 기호를 12개 나열했을 때, 로마 숫자로 인식 될 수 있는 숫자가 몇 개인지
# 구하시오. 예를 들어 1개의 기호로 표현할 수 있는 것은 I, V, X, L, C, D, M으로 모두
# 7가지, 15개의 기호로 표현할 수 있는 것은 'MMMDCCCLXXXVIII'(3,888)로 1가지

N = 12

def conv(n, i, v, x):
  result = ""
  if n == 9:
    result += i + x
  elif n == 4:
    result += i + v
  else:
    result += v * (n // 5)
    n = n % 5
    result += i * n
  return result

def roman(n):
  m, n = divmod(n, 1000)
  c, n = divmod(n, 100)
  x, n = divmod(n, 10)
  result = "M" * m
  result += conv(c, "C", "D", "M")
  result += conv(x, "X", "L", "C")
  result += conv(n, "I", "V", "X")
  return result

cnt = {}
for n in range(1, 4000):
  length = len(roman(n))
  if length in cnt:
    cnt[length] += 1
  else:
    cnt[length] = 1

print(cnt[N])