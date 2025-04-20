# 문제 링크 : https://www.acmicpc.net/problem/10807
# 간단한 문제 설명 : 
#   N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 세는 프로그램
#   입력 정수와 v는 -100 이상 100 이하
#
# 해결 방법 설명 : 
#   - N개의 정수를 리스트로 입력받음
#   - 찾을 정수 v를 입력받음
#   - 리스트를 순회하면서 v와 같은 수를 카운트
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 리스트 한 번 순회
#   - 공간 복잡도: O(N) - N개 정수 저장

N = int(input())
I = list(map(int, input().split()))
v = int(input())

count_int = 0
for i in I:
    if i == v:
        count_int += 1
print(count_int)