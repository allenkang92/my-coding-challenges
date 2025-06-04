# 문제 링크 : https://www.acmicpc.net/problem/11719
# 간단한 문제 설명 : 입력받은 내용을 그대로 출력하는 문제
# 해결 방법 설명 : sys.stdin.readlines()로 모든 입력을 읽고, 그대로 출력
# 시간/공간 복잡도 : O(N), N은 입력의 총 문자 수

import sys

# 모든 입력 라인 읽기
lines = sys.stdin.readlines()

# 읽은 내용 그대로 출력
for line in lines:
    # rstrip()을 사용하지 않고 그대로 출력 (줄바꿈 유지)
    print(line, end='')