# 문제 링크 : https://www.acmicpc.net/problem/11121
# 간단한 문제 설명 : 이진 대칭 채널을 통해 전송된 비트 문자열의 통신이 올바른지 확인하는 프로그램입니다.
# 해결 방법 설명 : 입력 문자열과 출력 문자열을 비교하여 일치 여부를 확인합니다.
# 시간/공간 복잡도 : O(T)

T = int(input())  # 전송 횟수

for _ in range(T):
    input_bits, output_bits = input().split()
    if input_bits == output_bits:
        print("OK")
    else:
        print("ERROR")