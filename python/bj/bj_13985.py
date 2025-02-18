# 문제 링크 (주석) : https://www.acmicpc.net/problem/13985
# 문제 설명:
#   "a + b = c"의 형식으로 주어진 산술 퀴즈의 답이 맞는지 확인하는 문제입니다.
#   a, b, c는 각각 한 자리 양의 정수입니다.
#
# 해결 방법 설명:
#   입력 문자열을 공백으로 분리하여 a, b, c를 추출하고,
#   a와 b의 합이 c와 같은지 비교합니다.
#   같으면 "YES", 그렇지 않으면 "NO"를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

inputs = input().split(" ")

if int(inputs[0]) + int(inputs[2]) == int(inputs[4]):
    print("YES")
else:
    print("NO")