# 문제 링크 (주석) : https://www.acmicpc.net/problem/28938
# 간단한 문제 설명 : 수열에 있는 각 숫자는 -1, 0, 1이며, 합에 따라 컨베이어의 이동 방향 결정
# 시간/공간 복잡도 : O(n)

n = int(input())
conv = list(map(int, input().split(" ")))
total = sum(conv)

if total < 0:
    print("Left")
elif total > 0:
    print("Right")
else:
    print("Stay")