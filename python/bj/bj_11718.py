# 문제 링크 : https://www.acmicpc.net/problem/11718
# 간단한 문제 설명 : 
#   입력받은 문자열을 그대로 출력하는 프로그램
#   최대 100줄, 각 줄은 100글자 이하
#
# 해결 방법 설명 : 
#   - while문으로 EOF까지 입력 받기
#   - try-except로 EOF 처리
#   - 입력받은 문자열을 그대로 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - N은 입력 줄 수
#   - 공간 복잡도: O(1) - 한 줄씩 처리

while True:
    try:
        print(input())
    except EOFError:
        break