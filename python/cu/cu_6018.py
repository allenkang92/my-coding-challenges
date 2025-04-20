# 문제 링크 : https://codeup.kr/problem.php?id=6018
# 간단한 문제 설명 : 시:분 형식의 시간을 입력받아 그대로 출력합니다.
# 해결 방법 설명 : 1. input().split(":")으로 시간과 분을 분리
#                2. print() 함수의 sep 매개변수를 사용하여 콜론으로 구분해 출력
# 시간/공간 복잡도 : O(1) (단순 입출력 연산)

hour, minute = input().split(":")  # 시간과 분을 콜론으로 구분하여 입력받기
print(hour, minute, sep=":")       # 콜론으로 구분하여 출력