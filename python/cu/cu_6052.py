# 문제 링크 : https://codeup.kr/problem.php?id=6052
# 간단한 문제 설명 : 정수를 입력받아 0이 아니면 True, 0이면 False를 출력합니다.
# 해결 방법 설명 : 1. input() 함수로 정수를 입력받습니다.
#                2. int() 함수로 입력값을 정수로 변환합니다.
#                3. bool() 함수를 사용하여 정수를 boolean 값으로 변환합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 형변환 연산)

n = int(input())

print(bool(n))