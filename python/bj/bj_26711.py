# 문제 링크 (주석) : https://www.acmicpc.net/problem/26711
# 간단한 문제 설명 :
#   매우 큰 두 양의 정수 (a, b)를 입력받아, a + b 의 합을 출력하는 문제입니다.
#   (각 정수는 최대 5,000자리까지 주어질 수 있습니다.)
#
# 해결 방법 설명 :
#   파이썬의 int는 임의 정밀도의 정수를 지원하므로, 매우 큰 수라도 int로 변환하여 덧셈 연산을 수행할 수 있습니다.
#   입력은 sys.stdin.readline() 을 사용하여 처리하며, 각 줄의 공백 및 줄바꿈 문자를 제거한 후 int로 변환합니다.
#
# 시간/공간 복잡도 : O(max(len(a), len(b)))

import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())

print(a + b)