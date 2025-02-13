# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6045
# 간단한 문제 설명 : 정수 3개를 입력받아 합과 평균을 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 세 수를 분리합니다.
#                2. map(int, ...)를 사용하여 각 수를 정수로 변환합니다.
#                3. 합과 평균을 계산합니다.
#                4. 결과를 출력합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 산술 연산)

a, b, c = map(int, input().split())

sum_value = a + b + c
avg_value = sum_value / 3

print(sum_value, format(avg_value, ".2f"))