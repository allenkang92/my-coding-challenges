# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6035
# 간단한 문제 설명 : 실수 2개를 입력받아 곱을 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(float, ...)를 사용하여 각 수를 실수로 변환합니다.
#                3. 두 수의 곱을 계산하여 출력합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 산술 연산)

f1, f2 = map(float, input().split())

print(f1 * f2)