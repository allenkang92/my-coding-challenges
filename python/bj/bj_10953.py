# 문제 링크 : https://www.acmicpc.net/problem/10953
# 간단한 문제 설명 : 두 정수 A와 B를 입력받아 A+B를 출력하는 문제 (A,B는 콤마로 구분됨)
# 해결 방법 설명 : 입력을 콤마(,)로 분리한 후 두 정수로 변환하여 합을 계산           
# 시간/공간 복잡도 : O(T), T는 테스트 케이스 개수

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # 콤마로 구분된 두 정수 입력받기
    A, B = map(int, input().split(','))
    
    # A+B 출력
    print(A + B)