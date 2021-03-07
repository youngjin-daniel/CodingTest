# 문제풀이 아이디어 :
# 모든 숫자는 어떤 수로 나누었을 때, 몫과 나머지로 구분됨.
# 1을 빼다가 나누어떨어질 때 나눗셈을 하는 것과
# 나눗셈을 하고 나머지를 1로 빼는 것은 결과적으로 같은 행위.

# N과 K를 공백을 기준으로 구분하여 입력
n, k = map(int, input().split())

# n을 loop내에서 감해나가는 계산에 사용할 변수에 저장
tmp = n
# count 초기화
count = 0

# 계속 나눗셈을 하다가, 나눠지는 값이 나누는 값보다 작으면 break
while True:

  # 몫과 나머지를 구함
  quot = tmp // k
  rem = tmp % k

  # 몫은 다음 loop의 나누는 대상의 값
  tmp = quot
  count += (1 + rem)

  if tmp < k:
    break

print(count)




