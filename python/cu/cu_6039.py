# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6039
# 간단한 문제 설명 : 실수 2개(f1, f2)를 입력받아 f1을 f2번 거듭제곱한 값을 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(float, ...)를 사용하여 각 수를 실수로 변환합니다.
#                3. f1**f2 연산자를 사용하여 거듭제곱을 계산합니다.
# 시간/공간 복잡도 : O(log f2) (거듭제곱 연산의 시간 복잡도)

f1, f2 = map(float, input().split())

print(f1 ** f2)