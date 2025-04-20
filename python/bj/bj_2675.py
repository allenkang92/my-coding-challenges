# 문제 링크 : https://www.acmicpc.net/problem/2675
# 간단한 문제 설명 : 
#   문자열 S의 각 문자를 R번 반복하여 새로운 문자열 P 생성
#   QR Code alphanumeric 문자만 입력으로 주어짐
#
# 해결 방법 설명 : 
#   - T개의 테스트 케이스를 입력받음
#   - 각 케이스마다:
#     - R과 S를 입력받음
#     - S의 각 문자를 R번 반복하여 P 생성
#     - P를 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(T*N*R) - T개 케이스, N길이 문자열, R번 반복
#   - 공간 복잡도: O(N*R) - 각 문자열을 R번 반복한 길이

T = int(input())

for _ in range(T):
    P = str()
    R, S = input().split(" ")
    R = int(R)
    
    for a in S:
        P += a * R

    print(P)