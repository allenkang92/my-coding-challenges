# 문제 링크 : https://codeup.kr/problem.php?id=6038
# 간단한 문제 설명 : 정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(int, ...)를 사용하여 각 수를 정수로 변환합니다.
#                3. a**b 연산자를 사용하여 거듭제곱을 계산합니다.
# 시간/공간 복잡도 : O(log b) (거듭제곱 연산의 시간 복잡도)

a, b = map(int, input().split())

print(a ** b)