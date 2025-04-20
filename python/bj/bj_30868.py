# 문제 링크 : https://www.acmicpc.net/problem/30868
# 간단한 문제 설명 : 후보자가 받은 표의 수에 따라 칠판에 그려지는 결과를 출력
# 해결 방법 설명 : 
#   1. 5로 나눈 몫만큼 "++++ "를 출력한다
#   2. 5로 나눈 나머지만큼 "|"를 출력한다
# 시간/공간 복잡도 : O(T * n) - T는 테스트 케이스 수, n은 각 후보의 표 수

# 입력 처리
T = int(input())
results = []

for _ in range(T):
    n = int(input())
    
    # 5로 나눈 몫과 나머지 계산
    five_groups = n // 5  # 5표 그룹 수
    remainder = n % 5     # 남은 표 수
    
    # 결과 문자열 생성
    result = ("++++ " * five_groups) + ("|" * remainder)
    
    results.append(result)

# 결과 출력
for result in results:
    print(result)