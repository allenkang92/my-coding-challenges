# 문제 링크 : https://codeup.kr/problem.php?id=6029
# 간단한 문제 설명 : 16진수 정수를 입력받아 8진수로 출력합니다.
# 해결 방법 설명 : 1. input() 함수로 16진수 정수를 입력받습니다.
#                2. int(a, 16) 함수로 16진수 문자열을 10진수 정수로 변환합니다.
#                3. %o 포맷 문자열을 사용하여 8진수로 출력합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 형변환 연산)

a = input()
n = int(a, 16)      # 입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  # n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력