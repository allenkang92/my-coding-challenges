# 문제 링크 (주석) : https://www.acmicpc.net/problem/11021
# 간단한 문제 설명 : 
#   테스트 케이스마다 두 정수 A와 B를 입력받아 A+B를 출력
#   각 케이스는 "Case #x: " 형식으로 출력
#
# 해결 방법 설명 : 
#   - T개의 테스트 케이스 수를 입력받음
#   - 각 케이스마다:
#     - A, B를 입력받아 합을 계산
#     - Case 번호와 함께 결과 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(T)
#   - 공간 복잡도: O(1)

T = int(input())

case_number = 0

for _ in range(T):
    A, B = map(int, input().split(" "))
    
    print(f"Case #{case_number+1}: ", A+B)
    case_number += 1