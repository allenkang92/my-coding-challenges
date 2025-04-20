# 문제 링크 : https://codeup.kr/problem.php?id=6055
# 간단한 문제 설명 : 두 정수를 입력받아 그 불 값이 하나라도 True일 때에만 True를 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(int, ...)를 사용하여 각 수를 정수로 변환합니다.
#                3. or 연산자를 사용하여 두 불 값 중 하나라도 True인지 확인합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 논리 연산)

a, b = map(int, input().split())

print(bool(a) or bool(b))