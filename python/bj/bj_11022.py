# 문제 링크 : https://www.acmicpc.net/problem/11022
# 간단한 문제 설명 : 
#   테스트 케이스마다 두 정수 A와 B를 입력받아 A+B를 출력
#   각 케이스는 "Case #x: A + B = C" 형식으로 출력 (C는 A+B의 결과)
#
# 해결 방법 설명 : 
#   - T개의 테스트 케이스 수를 입력받음
#   - 각 케이스마다:
#     - A, B를 입력받아 합을 계산
#     - 케이스 번호와 함께 A, B, 그리고 합을 형식에 맞춰 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(T) - T개의 테스트 케이스만큼 반복
#   - 공간 복잡도: O(1) - 상수 크기의 변수만 사용

T = int(input())

for i in range(T):
    A, B = map(int, input().split(" "))
    print(f"Case #{i + 1}: {A} + {B} = {A+B}")