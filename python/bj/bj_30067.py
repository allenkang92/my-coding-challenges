# 문제 링크 : https://www.acmicpc.net/problem/30067
# 간단한 문제 설명 : 
#   Simas가 9개의 정수를 생각하고 그 합을 계산한 다음, 10개의 숫자 중 하나로 숨김
#   10개의 숫자가 주어졌을 때, 어떤 숫자가 나머지 9개의 합인지 찾는 문제
#
# 해결 방법 설명 :            
#   만약 어떤 숫자 x가 나머지 9개 숫자의 합이라면:
#   x + (나머지 9개 합) = 전체 합
#   x + x = 전체 합
#   x = 전체 합 / 2
#   따라서 각 숫자를 검사하여 전체 합의 절반과 같은 숫자를 찾으면 됨
# 
# 시간/공간 복잡도 : O(N) - N은 숫자의 개수(10개로 고정)

# 10개의 숫자 입력 받기
numbers = []
for _ in range(10):
    numbers.append(int(input()))

# 모든 숫자의 합 계산
total_sum = sum(numbers)

# 각 숫자를 확인하여 숨겨진 합 찾기
for num in numbers:
    if num * 2 == total_sum:
        print(num)
        break