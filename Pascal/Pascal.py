# 파스칼의 삼각형과 동전의 개수
# 파스칼의 삼각형에서 각각의 값을 금액이라고 생각
# '1'은 1원, '2'는 2원, '10'은 10원. 이때 n번째
# 각각의 값에 대해서 동전/지폐의 최소 수를 생각하고
# 합계를 구함. 예를 들어 n = 4 라면 1, 4, 6, 4, 1로
# 정렬되며, 1원 = 1개, 4원 = 4개, 6원 = 2개(1원 동전 + 5원 동전)
# 이므로, 모두 더하면 12개. 마찬가지로 n = 9 일 때는 모두 48개
# n = 0                    1                     1개
# n = 1                   1 1                    2개
# n = 2                  1 2 1                   4개
# n = 3                 1 3 3 1                  8개
# n = 4                1 4 6 4 1                12개
# n = 45일 때, 동전/지폐 개수의 합을 구하시오.
  
n = 45

def counter(money):
  coin = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
  cnt = 0
  for c in coin:
    q, money = divmod(money, c)
    cnt += q
  return cnt

pascal_arr = [1] + n * [0]
for i in range(0, n):
  for j in range(i + 1, 0, -1):
    pascal_arr[j] += pascal_arr[j-1]

answer = 0
for i in range(len(pascal_arr)):
  answer += counter(pascal_arr[i])

print(answer)

