# 문제 링크 (주석) : https://www.acmicpc.net/problem/2562
# 간단한 문제 설명 : 
#   9개의 서로 다른 자연수가 주어질 때,
#   최댓값과 그 값이 몇 번째 수인지 출력
#
# 해결 방법 설명 : 
#   - 9개의 수를 리스트에 저장
#   - max() 함수로 최댓값을 한 번만 계산
#   - index() 함수로 위치 찾고 1을 더해서 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 리스트 순회
#   - 공간 복잡도: O(N) - 9개의 수 저장

numbers = []
for _ in range(9):
    numbers.append(int(input()))

max_value = max(numbers)
print(max_value)
print(numbers.index(max_value) + 1)