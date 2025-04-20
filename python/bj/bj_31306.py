# 문제 링크 : https://www.acmicpc.net/problem/31306
# 문제 설명:
#   주어진 문자열에서 y를 모음으로 고려하지 않았을 때와 고려했을 때의 모음의 개수를 각각 구하는 문제입니다.
#   모음은 a, e, i, o, u이며, y가 모음일 경우에는 추가로 y를 포함합니다.
#
# 해결 방법 설명:
#   문자열의 각 문자를 순회하면서, 해당 문자가 "aeiou"에 속하면 case1_count를 증가시키고,
#   "aeiouy"에 속하면 case2_count를 증가시킵니다.
#
# 시간/공간 복잡도 : O(N) 
line = input()

case1_count = 0
case2_count = 0
for ch in line:
    if ch in "aeiou":
        case1_count += 1
    if ch in "aeiouy":
        case2_count += 1
print(case1_count, case2_count)