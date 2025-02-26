# 문제 링크 (주석) : https://www.acmicpc.net/problem/15128
# 간단한 문제 설명 : 두 유리수가 주어졌을 때, 이를 직각삼각형의 두 변으로 했을 때 넓이가 정수인지 판단하세요.
# 해결 방법 설명 : (p1 * p2)가 (2 * q1 * q2)로 나누어떨어지는지 확인합니다.
# 시간/공간 복잡도 : O(1)

# 입력 받기
p1, q1, p2, q2 = map(int, input().split())

# 넓이가 정수인지 확인
numerator = p1 * p2
denominator = 2 * q1 * q2

# 결과 출력
if numerator % denominator == 0:
    print(1)
else:
    print(0)