# 문제 링크 : https://codeup.kr/problem.php?id=6040
# 간단한 문제 설명 : 정수 2개(a, b)를 입력받아 a를 b로 나눈 몫을 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(int, ...)를 사용하여 각 수를 정수로 변환합니다.
#                3. // 연산자를 사용하여 몫을 계산합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 산술 연산)

a, b = map(int, input().split())

print(a // b)