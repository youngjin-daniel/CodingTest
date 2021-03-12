# 풀이 자체 리뷰
# 일단, 답안예시가 훨씬 간단함
# 기술적인 면에서 개선 필요점
# 1. 받은 list의 순서가 기억될 필요가 없다면, list.sort() 사용이 메모리 관점에서 이득
# 2. pop을 사용하여 하나씩 끝까지 뽑아보는 것이라면, for문을 사용하는 것이 더 간결함
# 아이디어면에서 개선 필요점
# 1. sort되어 있는 list를 사용하기 때문에 tmp_n과 tmp_n_target을 비교하는 과정이 필요없고
#    그냥 tmp_n을 사용하면 됨 (즉, tmp_n_target이 필요없음)

n = int(input())
list_n = list(map(int, input().split()))

list_n_sorted = sorted(list_n)

group_count = 0

# temporary 변수
tmp_n = 0

tmp_n_target = 0
tmp_n_gathered = 0

while True:

  tmp_n = list_n_sorted.pop(0)
  
  if tmp_n > tmp_n_target:
    tmp_n_target = tmp_n

  tmp_n_gathered += 1
  
  if tmp_n_gathered == tmp_n_target:
    group_count += 1
    
    tmp_n_target = 0
    tmp_n_gathered = 0

  if not list_n_sorted:
    break

print(group_count)

