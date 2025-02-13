# 문제 링크 (주석) : https://codeup.kr/problem.php?id=6021
# 간단한 문제 설명 : 문자열을 입력받아 각 문자를 한 줄씩 출력합니다.
# 해결 방법 설명 : 1. 문자열을 입력받습니다.
#                2. 문자열의 각 문자를 순회하며 출력합니다.
# 시간/공간 복잡도 : O(N) (N은 문자열의 길이)

s = input()

for char in s:
    print(char)