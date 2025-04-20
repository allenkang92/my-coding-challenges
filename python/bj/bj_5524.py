# 문제 링크 : https://www.acmicpc.net/problem/5524
# 문제 설명:
#   JOI회사의 입실 기록으로 주어진 이름들을 모두 소문자로 변환하여 출력하는 문제입니다.
#
# 해결 방법 설명:
#   첫 줄에 입력된 정수 N을 이용하여, N개의 이름을 순서대로 읽고, 각 이름을 소문자로 변환하여 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())
for _ in range(N):
    name = input().strip().lower()
    print(name)