# 불이 켜진 세그먼트 개수로 예측해 보는 디지털 시계
# 12:34:56(12시 34분 56초)의 경우, 27개의 세그먼트에 불
# 디지털 시계는 24시간 형태로 출력, 23시 59분 59초까지
# 출력 가능하다. 또한, 시, 분, 초가 한 자릿수일 때는 빈
# 부분을 0으로 출력한다(예: 01:01:01). 30개의 세그먼트에
# 불이 들어왔을 경우, 예상할 수 있는 시각이 모두 몇가지 인가?

# 1
segment = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
answer = 0

def segment_counter(number):
  n, r = divmod(number, 10)
  return segment[n] + segment[r]

for h in range(0, 24):
  for m in range(0, 60):
    for s in range(0, 60):
      if segment_counter(h) + segment_counter(m) + segment_counter(s) == 30:
        answer += 1

print(answer)

# 2
segment = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
answer = 0

def segment_counter(number):
  n, r = divmod(number, 10)
  return segment[n] + segment[r]

lights = [0] * 60
for i in range(0, 60):
  lights[i] = segment_counter(i)

for h in range(0, 24):
  for m in range(0, 60):
    for s in range(0, 60):
      if lights[h] + lights[m] + lights[s] == 30:
        answer += 1

print(answer)