# 문제 링크 : https://codeup.kr/problem.php?id=6007
# 간단한 문제 설명 : print() 함수를 사용하여 Windows 파일 경로를 출력합니다.
# 해결 방법 설명 : 1. 백슬래시는 이스케이프 문자이므로 \\로 출력
#                2. 따옴표는 \"와 \'로 이스케이프 처리
# 시간/공간 복잡도 : O(1) (단순 출력 연산)

print("\"C:\\Download\\'hello\\'.py\"")