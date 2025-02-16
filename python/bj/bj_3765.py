# 문제 링크 (주석) : https://www.acmicpc.net/problem/3765
# 문제 설명:
#   입력으로 주어진 등식(solution) 그대로, 공백까지 동일하게 출력합니다.
#
# 해결 방법 설명:
#   입력의 각 줄을 그대로 출력합니다.
#
# 시간/공간 복잡도 : O(n)

import sys

for line in sys.stdin:
    print(line, end="")