# 문제 링크 : https://www.acmicpc.net/problem/10951
# 간단한 문제 설명 : 
#   두 정수 A와 B를 입력받아 합을 출력
#   입력이 끝날 때까지(EOF) 계속 진행
#
# 해결 방법 설명 : 
#   - while True로 무한 반복
#   - try-except로 EOFError 처리
#   - 입력이 끝나면(EOF) 프로그램 종료
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 입력 개수만큼 반복
#   - 공간 복잡도: O(1) - 상수 공간만 사용

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break