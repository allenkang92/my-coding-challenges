# 문제 링크 : https://codeup.kr/problem.php?id=6020
# 간단한 문제 설명 : 주민번호 입력받아 '-'를 제거하고 출력합니다.
# 해결 방법 설명 : 1. input() 함수로 주민번호 입력받기
#                2. replace() 함수로 '-' 문자 제거
#                3. 결과 출력
# 시간/공간 복잡도 : O(1) (문자열 길이 상수)

num = input()           # 주민번호 입력
num = num.replace("-", "")  # '-' 문자 제거
print(num)              # 결과 출력