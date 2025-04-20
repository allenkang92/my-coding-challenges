# 문제 링크 : https://www.acmicpc.net/problem/4589
# 간단한 문제 설명 :
#   주어진 각 그룹의 세 정수(각 그룹은 gnome들의 수염 길이)가 오름차순이나 내림차순이면 "Ordered",
#   아니라면 "Unordered"를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   입력된 각 그룹에 대해, 리스트가 정렬된 상태 또는 역순으로 정렬된 상태인지 판단하여 출력합니다.
#
# 시간/공간 복잡도 : O(N)
 
N = int(input())
 
print("Gnomes:")
for _ in range(N):
    line = list(map(int, input().split()))
    if line == sorted(line) or line == sorted(line, reverse=True):
        print("Ordered")
    else:
        print("Unordered")