# 문제 링크 : https://codeup.kr/problem.php?id=6056
# 간단한 문제 설명 : 두 정수를 입력받아 그 불 값이 서로 다를 때에만 True 를 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(int, ...)를 사용하여 각 수를 정수로 변환합니다.
#                3. 두 값의 bool 값을 비교하여 서로 다를 경우 True를 출력합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 비교 연산)

a, b = map(int, input().split())

print(bool(a) != bool(b))