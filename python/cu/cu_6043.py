# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6043
# 간단한 문제 설명 : 실수 2개(f1, f2)를 입력받아 f1을 f2로 나눈 값을 소수점 넷째 자리에서 반올림하여 소수점 셋째 자리까지 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(float, ...)를 사용하여 각 수를 실수로 변환합니다.
#                3. ZeroDivisionError 예외 처리를 추가합니다.
#                4. f1 / f2를 계산하고 format() 함수를 사용하여 소수점 셋째 자리까지 출력합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 산술 연산)

try:
    f1, f2 = map(float, input().split())
    result = f1 / f2
    print(format(result, ".3f"))
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")