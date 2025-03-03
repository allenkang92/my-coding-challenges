# 문제 링크 (주석) : https://www.acmicpc.net/problem/27332
# 간단한 문제 설명 : 2022년 11월 A일에 B주일 후의 날짜가 여전히 2022년 11월인지 확인
# 해결 방법 설명 : A일에 7 * B일을 더한 날짜가 1일부터 30일 사이인지 확인
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
A = int(input())
B = int(input())

# 날짜 계산
future_day = A + 7 * B

# 11월 확인 (1일부터 30일 사이인지)
if 1 <= future_day <= 30:
    print(1)
else:
    print(0)