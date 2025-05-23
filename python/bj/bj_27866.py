# 문제 링크 : https://www.acmicpc.net/problem/27866
# 간단한 문제 설명 : 
#   문자열 S와 위치 i가 주어지면 i번째 문자를 출력
#
# 해결 방법 설명 : 
#   - 문자열 S와 정수 i를 입력받음
#   - 파이썬 인덱스는 0부터 시작하므로 i-1번째 문자 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1) - 문자열 인덱싱
#   - 공간 복잡도: O(1) - 상수 공간만 사용

S = input()
i = int(input())

print(S[i-1])  # i번째 문자는 인덱스 i-1