# 이렇게 하면 틀리는 이유
# 0, 1, 2의 경우, 0 + 1 = 1인데 이를 2와 곱하게 됨
# 0, 0, 1, 2의 경우도 마찬가지
# 초기값들만 확인이 필요한 것이 아니라 이전 연산 결과를 check하는 것이
# 일관되고 모두 커버할 수 있는 맞는 코드

list_num = list( map(int, input()) )

print(list_num)

# 초기값 처리
if list_num[0] <= 1 or list_num[1] <= 1:
  tmp = list_num[0] + list_num[1]
else:
  tmp = list_num[0] * list_num[1]

for i in list_num[2:]:

  if i == 0 or i == 1:
    tmp += i
  else:
    tmp *= i 

result = tmp
print(result)
