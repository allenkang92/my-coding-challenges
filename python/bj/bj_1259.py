# 문제 링크 : https://www.acmicpc.net/problem/1259
# 간단한 문제 설명 : 주어진 수가 앞에서 읽으나 뒤에서 읽으나 같은 팰린드롬수인지 판별하는 문제
# 해결 방법 설명 : 입력받은 문자열을 뒤집어서 원래 문자열과 같은지 비교
# 시간/공간 복잡도 : O(n), n은 입력 문자열의 길이

# 여러 테스트 케이스를 처리
while True:
    # 한 줄 입력 받기
    line = input()
    
    # 종료 조건: 입력이 "0"이면 종료
    if line == "0":
        break

    # 문자열을 뒤집어서 원래 문자열과 같은지 비교
    # line[::-1]은 문자열을 뒤집는 Python 슬라이싱 기법
    if line == line[::-1]:
        print("yes")
    else:
        print("no")